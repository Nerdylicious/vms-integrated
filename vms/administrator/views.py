from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

@login_required
def settings(request):
    return render(request, 'administrator/settings.html')
