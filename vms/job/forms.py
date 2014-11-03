from django import forms
from django.db import models
from django.forms import ModelForm
from job.models import Job

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'start_date', 'end_date', 'description']
