from django.core.validators import RegexValidator
from django.db import models
from job.models import Job

class Shift(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_volunteers = models.PositiveSmallIntegerField(
        validators=[
            RegexValidator(
                r'^[0-9]+$',
            ),
        ],
    )
    #Job to Shift is a one-to-many relationship
    job = models.ForeignKey(Job)
