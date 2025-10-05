from django.db.models import Q
from django.utils.translation import gettext as _
from .models import NSOService, NSOServiceInstance

def search_services(query):
    """
    Search for services based on the provided query.
    """
    return NSOService.objects.filter(Q(name__icontains=query))

def search_service_instances(query):
    """
    Search for service instances based on the provided query.
    """
    return NSOServiceInstance.objects.filter(Q(name__icontains=query) | Q(service__name__icontains=query))