from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from job.services import *
from shift.forms import ShiftForm
from shift.models import Shift
from shift.services import *

@login_required
def create(request, job_id):
    if job_id:
        if request.method == 'POST':
            job = get_job_by_id(job_id)
            if job:
                form = ShiftForm(request.POST)
                if form.is_valid():
                    shift = form.save(commit=False)
                    shift.job = job
                    shift.save()
                    return HttpResponseRedirect(reverse('shift:list_shifts', args=(job_id,)))
                else:
                    return render(request, 'shift/create.html', {'form' : form, 'job_id' : job_id,})
            else:
                raise Http404
        else:
            form = ShiftForm()
            return render(request, 'shift/create.html', {'form' : form, 'job_id' : job_id,})
    else:
        raise Http404

@login_required
def delete(request, shift_id):

    if request.method == 'POST':
        result = delete_shift(shift_id)
        if result:
            return HttpResponseRedirect(reverse('shift:list_jobs'))
        else:
            return render(request, 'shift/delete_error.html')
    return render(request, 'shift/delete.html', {'shift_id' : shift_id})

@login_required
def edit(request, shift_id):

    shift = None
    if shift_id:
        shift = get_shift_by_id(shift_id)

    if request.method == 'POST':
        form = ShiftForm(request.POST, instance=shift)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('shift:list_shifts', args=(shift.job.id,)))
        else:
            return render(request, 'shift/edit.html', {'form' : form, 'shift' : shift})
    else:
        form = ShiftForm(instance=shift)
        return render(request, 'shift/edit.html', {'form' : form, 'shift' : shift})

@login_required
def list_jobs(request):
    job_list = get_jobs_ordered_by_title()
    return render(request, 'shift/list_jobs.html', {'job_list' : job_list})

@login_required
def list_shifts(request, job_id):
    if job_id:
        job = get_job_by_id(job_id)
        if job:
            shift_list = get_shifts_ordered_by_date(job_id)
            return render(request, 'shift/list_shifts.html', {'shift_list' : shift_list, 'job_id' : job_id})
        else:
            raise Http404
    else:
        raise Http404

@login_required
def list_shifts_sign_up(request, job_id):
    if job_id:
        job = get_job_by_id(job_id)
        if job:
            shift_list = get_shifts_by_job_id(job_id) 
            return render(request, 'shift/list_shifts_sign_up.html', {'shift_list' : shift_list, 'job' : job})
        else:
            raise Http404
    else:
        raise Http404

@login_required
def sign_up(request, shift_id):
    if shift_id:
        shift = get_shift_by_id(shift_id)
        if shift:
            if request.method == 'POST':
                #retrieve the logged in user.id and from this retrieve the corresponding volunteer.id
                user = request.user
                if user.is_authenticated():
                    volunteer_id = user.volunteer.id
                    try:
                        register(volunteer_id, shift_id)            
                        return HttpResponse('registered')
                    except ObjectDoesNotExist:
                        raise Http404
                    except Exception as e:
                        if str(e) == 'No slots remaining':
                            return HttpResponse('No slots remaining')
                        if str(e) == 'Is already signed up':
                            return HttpResponse('Signed up for this shift already')
                        return HttpResponse('An error has occurred')
                else:
                    #return an Http 403 Forbidden code
                    return HttpResponse(status=403)
            else:
                return render(request, 'shift/sign_up.html', {'shift' : shift})
        else:
            raise Http404
    else:
        raise Http404
        
@login_required
def view_volunteer_shifts(request, volunteer_id):
    if volunteer_id:
        volunteer = get_volunteer_by_id(volunteer_id)
        if volunteer:
            user = request.user
            if int(user.volunteer.id) == int(volunteer_id):
                shift_list = get_shifts_signed_up_for(volunteer_id)
                return render(request, 'shift/volunteer_shifts.html', {'shift_list' : shift_list, 'volunteer_id' : volunteer_id,})
            else:
                return HttpResponse(status=403)
        else:
            raise Http404
    else:
        raise Http404
