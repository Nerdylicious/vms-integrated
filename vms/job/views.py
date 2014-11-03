from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

@login_required
def create(request):
    return render(request, 'job/create.html')

@login_required
def list(request):
    return render(request, 'job/list.html')
