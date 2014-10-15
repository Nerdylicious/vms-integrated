from django.conf.urls import patterns, url
from event import views

urlpatterns = patterns('',
    url(r'^list/$', views.list, name='list'),
)
