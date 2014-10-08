from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from organization.forms import OrganizationForm
from organization.services import *

@login_required
def list(request):
    organization_list = get_organizations_ordered_by_name()
    return render(request, 'organization/list.html')
