import os
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.servers.basehttp import FileWrapper
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from organization.services import *
from volunteer.forms import * 
from volunteer.models import Volunteer
from volunteer.validation import *

@login_required
def profile(request, volunteer_id):

    volunteer = get_volunteer_by_id(volunteer_id)
    if volunteer:
        user = request.user
        if int(user.volunteer.id) == int(volunteer_id):
            return render(request, 'volunteer/profile.html', {'volunteer' : volunteer})
        else:
            return HttpResponse(status=403)
    else:
        #if Http404 is raised at any point in a view function, Django will catch it and return the standard
        #error page, along with an HTTP error code 404
        raise Http404
