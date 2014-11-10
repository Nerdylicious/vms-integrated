from django.conf.urls import patterns, url
from shift import views

urlpatterns = patterns('',
    url(r'^list/$', views.list, name='list'),
)
