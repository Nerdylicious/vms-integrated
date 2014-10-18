from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from event.forms import EventForm

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

@login_required
def list(request):
    return render(request, 'event/list.html')
