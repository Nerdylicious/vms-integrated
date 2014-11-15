from django.core.validators import RegexValidator
from django.db import models
from job.models import Job

class Shift(models.Model):
    address = models.CharField(
        max_length=75,
        validators=[
            RegexValidator(
                r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\-)]+$',
            ),
        ],
    )
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
