import datetime
from django.core.exceptions import ObjectDoesNotExist
from job.models import Job
from shift.models import Shift, VolunteerShift
from volunteer.services import *

def add_shift_hours(v_id, s_id, start_time, end_time):

    volunteer_shift = get_volunteer_shift_by_id(v_id, s_id)

    if volunteer_shift:
        volunteer_shift.start_time = start_time
        volunteer_shift.end_time = end_time
        volunteer_shift.save()
    else:
        raise ObjectDoesNotExist

def cancel_shift_registration(v_id, s_id):

    if s_id and v_id:
        try:
            shift = Shift.objects.get(pk=s_id)
            obj = VolunteerShift.objects.get(volunteer_id=v_id, shift_id=s_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist
        else:
            #remove volunteer from being signed up for this shift
            obj.delete()
    else:
        raise TypeError

def clear_shift_hours(v_id, s_id):

    result = True
    volunteer_shift = get_volunteer_shift_by_id(v_id, s_id)

    if volunteer_shift:
        volunteer_shift.start_time = None
        volunteer_shift.end_time = None
        volunteer_shift.save()
    else:
        result = False
    
    return result

def delete_shift(shift_id):

    result = True
    shift = get_shift_by_id(shift_id)

    if shift:
        shift.delete()
    else:
        result = False

    return result

def edit_shift_hours(v_id, s_id, start_time, end_time):

    volunteer_shift = get_volunteer_shift_by_id(v_id, s_id)

    if volunteer_shift:
        volunteer_shift.start_time = start_time
        volunteer_shift.end_time = end_time
        volunteer_shift.save()
    else:
        raise ObjectDoesNotExist

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

def get_shifts_with_open_slots(j_id):

    shift_list_by_date = get_shifts_ordered_by_date(j_id)
    shift_list = []

    for shift in shift_list_by_date:
        if get_shift_slots_remaining(shift.id) > 0:
            shift_list.append(shift)

    return shift_list             
    
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

def get_volunteer_shifts_with_hours(v_id):

    #get shifts that the volunteer is signed up for
    volunteer_shift_list = VolunteerShift.objects.filter(volunteer_id=v_id)

    #get shifts that have logged hours only
    volunteer_shift_list = volunteer_shift_list.filter(start_time__isnull=False, end_time__isnull=False)

    #order by date, start_time and end_time in descending order
    volunteer_shift_list = volunteer_shift_list.order_by('-shift__date', '-start_time', '-end_time')

    return volunteer_shift_list
    
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
