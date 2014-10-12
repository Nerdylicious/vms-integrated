from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from organization.models import Organization

def delete_organization(organization_id):

    organization = get_organization_by_id(organization_id)
    
    if organization:
        organization.delete()
    else:
        return ObjectDoesNotExist

def get_organization_by_id(organization_id):
    
    is_valid = True
    result = None

    try:
        organization = Organization.objects.get(pk=organization_id)
    except ObjectDoesNotExist:
        is_valid = False

    if is_valid:
        result = organization

    return result

#organization names must unique
def get_organization_by_name(organization_name):

    is_valid = True
    result = None

    try:
        organization = Organization.objects.get(name__icontains=organization_name)
    except MultipleObjectsReturned:
        is_valid = False
    except ObjectDoesNotExist:
        is_valid = False

    if is_valid:
        result = organization

    return result

def get_organizations_ordered_by_name():
    organization_list = Organization.objects.all().order_by('name')
    return organization_list
