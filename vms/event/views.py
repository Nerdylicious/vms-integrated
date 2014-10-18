from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from event.forms import EventForm
from event.services import *

@login_required
def create(request):

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('event:list'))
        else:
            return render(request, 'event/create.html', {'form' : form,})
    else:
        form = EventForm()
        return render(request, 'event/create.html', {'form' : form,})

def edit(request):
    return render(request, 'event/edit.html')

@login_required
def list(request):
    event_list = get_events_ordered_by_name()
    return render(request, 'event/list.html', {'event_list' : event_list})
