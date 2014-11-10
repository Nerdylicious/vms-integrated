import datetime
from django.core.exceptions import ObjectDoesNotExist
from job.models import Job
from volunteer.services import *

def get_shifts_ordered_by_date(j_id):
    shift_list = Shift.objects.filter(job_id=j_id).order_by('date')
    return shift_list
