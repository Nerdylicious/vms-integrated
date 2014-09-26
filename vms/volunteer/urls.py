from django.conf.urls import patterns, url
from volunteer import views

urlpatterns = patterns('',
    url(r'^profile/(?P<volunteer_id>\d+)/$', views.profile, name='profile'),
)
