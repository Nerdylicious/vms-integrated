from django.conf.urls import patterns, url
from volunteer import views

urlpatterns = patterns('',
    url(r'^download_resume/(?P<volunteer_id>\d+)$', views.download_resume, name='download_resume'),
    url(r'^edit/(?P<volunteer_id>\d+)$', views.edit, name='edit'),
    url(r'^profile/(?P<volunteer_id>\d+)$', views.profile , name='profile'),
)
