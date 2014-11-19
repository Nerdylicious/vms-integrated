import datetime
from django.core.exceptions import ObjectDoesNotExist
from job.models import Job
from shift.models import Shift
from volunteer.services import *

def delete_shift(shift_id):

    result = True
    shift = get_shift_by_id(shift_id)

    if shift:
        shift.delete()
    else:
        result = False

    return result

def get_shift_by_id(shift_id):

    is_valid = True
    result = None

    try:
        shift = Shift.objects.get(pk=shift_id)
    except ObjectDoesNotExist:
        is_valid = False

    if is_valid:
        result = shift

    return result

def get_shifts_ordered_by_date(j_id):
    shift_list = Shift.objects.filter(job_id=j_id).order_by('date')
    return shift_list
