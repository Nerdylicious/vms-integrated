from django import forms
from django.db import models
from django.forms import ModelForm
from administrator.models import Administrator

class AdministratorForm(ModelForm):
    class Meta:
        model = Administrator
        fields = ['first_name', 'last_name', 'address', 'city', 'state', 'country', 'phone_number', 'unlisted_organization', 'email']
