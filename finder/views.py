from django.shortcuts import render, redirect
from .models import Search
from .forms import SearchForm
import requests


def index(request):
    searches = Search.objects.all()
    count = Search.objects.all().count()
    return render(request, 'finder/index.html', {'searches': searches, 'count': count})


def new_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        proxyDict = {
            'http': "add http proxy",
            'https': "add https proxy"
        }
        if form.is_valid():
            term = form.save(commit=False)
            ji = []
            url = 'https://search.torre.co/opportunities/_search/?[offset=&size=1000&aggregate=]'
            x = requests.post(url, proxies=proxyDict)
            for i in x.json()["results"]:
                for c in i["skills"]:
                    if c["name"] == term.text:
                        ji.append(i["id"])
            term.jobsid = ji
            term.save()
            return redirect('index')
        else:
            form = SearchForm()
            return render(request, 'finder/search.html', {'form': form})

    else:
        form = SearchForm()
        return render(request, 'finder/search.html', {'form': form})
