from django.conf.urls import patterns, url
from event import views

urlpatterns = patterns('',
    url(r'^create/$', views.create, name='create'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^list/$', views.list, name='list'),
)
