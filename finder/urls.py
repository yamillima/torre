from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.new_search, name='new_search'),
    url(r'^index', views.index, name='index'),
    url(r'^results', views.results, name='results'),
    url(r'^failed_search', views.failed_search, name='failed_search'),
]
