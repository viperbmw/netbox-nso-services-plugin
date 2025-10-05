from netbox.api.viewsets import NetBoxModelViewSet
from nso_services.api.serializers import NSOServiceSerializer, NSOServiceInstanceSerializer
from nso_services.models import NSOService, NSOServiceInstance
from nso_services import filtersets

class NSOServiceViewSet(NetBoxModelViewSet):
    queryset = NSOService.objects.all().order_by('id')
    serializer_class = NSOServiceSerializer
    filterset_class = filtersets.ServiceFilter

class NSOServiceInstanceViewSet(NetBoxModelViewSet):
    queryset = NSOServiceInstance.objects.all().order_by('id')
    serializer_class = NSOServiceInstanceSerializer
    filterset_class = filtersets.ServiceInstanceFilter