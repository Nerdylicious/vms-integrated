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
from volunteer.services import * 
from volunteer.validation import *

@login_required
def download_resume(request, volunteer_id):
    user = request.user
    if int(user.volunteer.id) == int(volunteer_id):
        if request.method == 'POST':
            basename = get_volunteer_resume_file_url(volunteer_id)
            if basename:
                filename = settings.MEDIA_ROOT + basename 
                wrapper = FileWrapper(file(filename))
                response = HttpResponse(wrapper)
                response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(filename)
                response['Content-Length'] = os.path.getsize(filename)
                return response
            else:
                raise Http404
    else:
        return HttpResponse(status=403)
        
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
