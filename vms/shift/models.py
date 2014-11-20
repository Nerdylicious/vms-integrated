from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from job.models import Job

class Shift(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_volunteers = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5000)
        ]
    )
    #Job to Shift is a one-to-many relationship
    job = models.ForeignKey(Job)
