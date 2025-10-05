from django_filters import FilterSet, CharFilter, ModelChoiceFilter
from .models import NSOService, NSOServiceInstance

class ServiceFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = NSOService
        fields = ['name']

class ServiceInstanceFilter(FilterSet):
    service = ModelChoiceFilter(queryset=NSOService.objects.all())
    instance_name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = NSOServiceInstance
        fields = ['service', 'instance_name']