from django.conf.urls import patterns, url
from shift import views

urlpatterns = patterns('',
    url(r'^create/$', views.create, name='create'),
    url(r'^list_jobs/$', views.list_jobs, name='list_jobs'),
)
