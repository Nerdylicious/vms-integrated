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
