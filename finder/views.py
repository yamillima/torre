from django.shortcuts import render, redirect
from .models import Search
from .forms import SearchForm


def index(request):
    searches = Search.objects.all()
    count = Search.objects.all().count()
    return render(request, 'finder/index.html', {'searches': searches, 'count': count})


def new_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            save = form.save()
            return redirect('index')
        else:
            form = SearchForm()
            return render(request, 'finder/search.html', {'form': form})

    else:
        form = SearchForm()
        return render(request, 'finder/search.html', {'form': form})
