import datetime
from django.core.exceptions import ObjectDoesNotExist
from job.models import Job
from shift.models import Shift, VolunteerShift
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

def get_shifts_by_job_id(j_id):
    shift_list = Shift.objects.filter(job_id=j_id)
    return shift_list

def get_shifts_ordered_by_date(j_id):
    shift_list = Shift.objects.filter(job_id=j_id).order_by('date')
    return shift_list

def get_shifts_signed_up_for(v_id):

     shift_signed_up_list = Shift.objects.filter(volunteershift__volunteer_id=v_id).order_by('date')
     return shift_signed_up_list

def get_shift_slots_remaining(s_id):

    shift = get_shift_by_id(s_id)
    num_total_slots = shift.max_volunteers
    num_slots_taken = VolunteerShift.objects.filter(shift_id=s_id).count()
    num_slots_remaining = num_total_slots - num_slots_taken

    return num_slots_remaining
    
def get_volunteer_shift_by_id(v_id, s_id):
    
    is_valid = True
    result = None

    try:
        volunteer_shift = VolunteerShift.objects.get(volunteer_id=v_id, shift_id=s_id)
    except ObjectDoesNotExist:
        is_valid = False

    if is_valid:
        result = volunteer_shift

    return result
    
def is_signed_up(v_id, s_id):

    result = True

    volunteer_shift = get_volunteer_shift_by_id(v_id, s_id)
    if not volunteer_shift:
        result = False 

    return result
    
def register(v_id, s_id):

    result = "IS_VALID"
    ERROR_CODE_ALREADY_SIGNED_UP = "ERROR_CODE_ALREADY_SIGNED_UP"
    ERROR_CODE_NO_SLOTS_REMAINING = "ERROR_CODE_NO_SLOTS_REMAINING"

    #a volunteer must not be allowed to register for a shift that they are already registered for
    signed_up = is_signed_up(v_id, s_id)

    if not signed_up:

        volunteer_obj = get_volunteer_by_id(v_id)
        shift_obj = get_shift_by_id(s_id) 

        if volunteer_obj and shift_obj:

            num_slots_remaining = get_shift_slots_remaining(s_id)

            if num_slots_remaining > 0:

                registration_obj = VolunteerShift(volunteer=volunteer_obj, shift=shift_obj)
                registration_obj.save()

            else:
                result = ERROR_CODE_NO_SLOTS_REMAINING
        else:
            raise ObjectDoesNotExist
    else:
        result = ERROR_CODE_ALREADY_SIGNED_UP

    return result
