from rest_framework import serializers
from netbox.api.serializers import WritableNestedSerializer
from nso_services.models import NSOService, NSOServiceInstance


class NestedNSOServiceSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:nso_services-api:nsoservice-detail')

    class Meta:
        model = NSOService
        fields = ['id', 'url', 'display', 'name']


class NestedNSOServiceInstanceSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:nso_services-api:nsoserviceinstance-detail')
    service = NestedNSOServiceSerializer(read_only=True)

    class Meta:
        model = NSOServiceInstance
        fields = ['id', 'url', 'display', 'name', 'service']
