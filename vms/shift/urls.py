from django.conf.urls import patterns, url
from shift import views

urlpatterns = patterns('',
    url(r'^create/(?P<job_id>\d+)$', views.create, name='create'),
    url(r'^delete/(?P<shift_id>\d+)$', views.delete, name='delete'),
    url(r'^list_jobs/$', views.list_jobs, name='list_jobs'),
    url(r'^list_shifts/(?P<job_id>\d+)$', views.list_shifts, name='list_shifts'),
)
