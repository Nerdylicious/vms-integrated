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

@login_required
def edit(request, job_id):

    job = None
    if job_id:
        job = get_job_by_id(job_id)

    event_list = get_events_ordered_by_name()

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            job_to_edit = form.save(commit=False)
            event_id = request.POST.get('event_id')
            event = get_event_by_id(event_id)
            if event:
                job_to_edit.event = event
            else:
                raise Http404
            job_to_edit.save()
            return HttpResponseRedirect(reverse('job:list'))
        else:
            return render(request, 'job/edit.html', {'form' : form, 'event_list' : event_list, 'job' : job})
    else:            
        form = JobForm(instance=job)
        return render(request, 'job/edit.html', {'form' : form, 'event_list' : event_list, 'job' : job})

@login_required
def list(request):
    job_list = get_jobs_ordered_by_title()
    return render(request, 'job/list.html', {'job_list' : job_list})
