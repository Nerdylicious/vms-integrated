from django import forms
from django.db import models
from django.forms import ModelForm
from volunteer.models import Volunteer

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'address', 'city', 'state', 'country', 'phone_number', 'unlisted_organization', 'email', 'websites', 'description', 'resume', 'resume_file']
