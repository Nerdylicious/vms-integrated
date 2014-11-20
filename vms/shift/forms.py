from django import forms
from django.db import models
from django.forms import ModelForm
from shift.models import Shift

class ShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields = ['date', 'start_time', 'end_time', 'max_volunteers']     
