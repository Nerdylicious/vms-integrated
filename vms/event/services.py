from django.core.exceptions import ObjectDoesNotExist
from event.models import Event

def get_event_by_id(event_id):

    is_valid = True
    result = None

    try:
        event = Event.objects.get(pk=event_id)
    except ObjectDoesNotExist:
        is_valid = False

    if is_valid:
        result = event

    return result

def get_events_ordered_by_name():
    event_list = Event.objects.all().order_by('name')
    return event_list
