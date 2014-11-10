from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from job.services import *

@login_required
def create(request):
    return render(request, 'shift/create.html')

@login_required
def list_jobs(request):
    job_list = get_jobs_ordered_by_title()
    return render(request, 'shift/list_jobs.html', {'job_list' : job_list})

@login_required
def list_shifts(request):
    return render(request, 'shift/list_shifts.html')
