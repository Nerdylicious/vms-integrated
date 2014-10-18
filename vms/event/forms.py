from django import forms
from django.db import models
from django.forms import ModelForm
from event.models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date']
