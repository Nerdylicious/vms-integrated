from django.conf.urls import patterns, url
from registration import views

urlpatterns = patterns('',
    url(r'^administrator/$', views.signup_administrator, name='signup_administrator'),
    url(r'^volunteer/$', views.signup_volunteer, name='signup_volunteer'),
)
