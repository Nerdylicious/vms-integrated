from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from job.models import Job
from job.forms import JobForm
from job.services import *
from event.services import *

@login_required
def create(request):

    event_list = get_events_ordered_by_name()

    if event_list:
        if request.method == 'POST':
            form = JobForm(request.POST)
            if form.is_valid():

                job = form.save(commit=False)

                event_id = request.POST.get('event_id')
                event = get_event_by_id(event_id)

                if event:
                    job.event = event
                else:
                    raise Http404

                job.save()
                return HttpResponseRedirect(reverse('job:list'))
            else:
                return render(request, 'job/create.html', {'form' : form, 'event_list' : event_list})
        else:
            form = JobForm()
            return render(request, 'job/create.html', {'form' : form, 'event_list' : event_list})
    else:
        raise Http404

@login_required
def list(request):
    job_list = get_jobs_ordered_by_title()
    return render(request, 'job/list.html', {'job_list' : job_list})
