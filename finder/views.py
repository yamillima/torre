from django.shortcuts import render, redirect
from .models import Search
from .forms import SearchForm
import requests
import ast


def index(request):
    searches = Search.objects.all()
    count = Search.objects.all().count()
    return render(request, 'finder/index.html', {'searches': searches, 'count': count})


def new_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            term = form.save(commit=False)
            ji = []
            url = 'https://search.torre.co/opportunities/_search/?[offset=&size=1000&aggregate=]'
            x = requests.post(url)
            for i in x.json()["results"]:
                for c in i["skills"]:
                    if c["name"] == term.text:
                        ji.append(i["id"])
            term.jobsid = ji
            term.save()
            return redirect('results')
        else:
            form = SearchForm()
            return render(request, 'finder/search.html', {'form': form})
    else:
        form = SearchForm()
        return render(request, 'finder/search.html', {'form': form})


def results(request):
    search = Search.objects.latest("jobsid")
    words = search.text
    ids = ast.literal_eval(search.jobsid)
    jobs = []
    orgs = []
    pics = []
    counter = -1
    if len(ids) > 2:
        for i in ids:
            counter = counter + 1
            if counter < 3:
                url = 'https://torre.co/api/opportunities/'+i
                x = requests.get(url).json()
                jobs.append(x["objective"])
                orgs.append(x["organizations"][0]["name"])
                pics.append(x["organizations"][0]["picture"])
        dict1 = {"jobs": [[jobs[0]]], "orgs": [[orgs[0]]], "pics": [[pics[0]]]}
        dict2 = {"jobs": [[jobs[1]]], "orgs": [[orgs[1]]], "pics": [[pics[1]]]}
        dict3 = {"jobs": [[jobs[2]]], "orgs": [[orgs[2]]], "pics": [[pics[2]]]}
        return render(request, 'finder/results.html', {'words': words, 'dict1': dict1, 'dict2': dict2, 'dict3': dict3, 'jobs': jobs, 'orgs': orgs, 'pics': pics})
    else:
        return redirect('failed_search')

def failed_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            term = form.save(commit=False)
            ji = []
            url = 'https://search.torre.co/opportunities/_search/?[offset=&size=1000&aggregate=]'
            x = requests.post(url)
            for i in x.json()["results"]:
                for c in i["skills"]:
                    if c["name"] == term.text:
                        ji.append(i["id"])
            term.jobsid = ji
            term.save()
            return redirect('results')
        else:
            form = SearchForm()
            return render(request, 'finder/failed_search.html', {'form': form})
    else:
        form = SearchForm()
        return render(request, 'finder/failed_search.html', {'form': form})
