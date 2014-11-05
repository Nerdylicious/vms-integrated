from django.conf.urls import patterns, url
from job import views

urlpatterns = patterns('',
    url(r'^create/$', views.create, name='create'),
    url(r'^edit/(?P<job_id>\d+)$', views.edit, name='edit'),
    url(r'^list/$', views.list, name='list'),
)
