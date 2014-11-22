from django.conf.urls import patterns, url
from shift import views

urlpatterns = patterns('',
    url(r'^create/(?P<job_id>\d+)$', views.create, name='create'),
    url(r'^delete/(?P<shift_id>\d+)$', views.delete, name='delete'),
    url(r'^edit/(?P<shift_id>\d+)$', views.edit, name='edit'),
    url(r'^list_jobs/$', views.list_jobs, name='list_jobs'),
    url(r'^list_shifts/(?P<job_id>\d+)$', views.list_shifts, name='list_shifts'),
    url(r'^list_shifts_sign_up/(?P<job_id>\d+)$', views.list_shifts_sign_up, name='list_shifts_sign_up'),
)
