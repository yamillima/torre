from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.new_search, name='new_search'),
    url(r'^index', views.index, name='index'),
]
