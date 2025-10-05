from rest_framework import serializers
from django.db.models import Q
from dcim.models import Device
from nso_services.models import NSOServiceInstance
from nso_services.api.nested_serializers import NestedNSOServiceInstanceSerializer


class DeviceNSOServicesField(serializers.SerializerMethodField):
    """Custom field to show NSO service instances assigned to a device"""

    def get_attribute(self, instance):
        # Return the whole instance so we can query related objects
        return instance

    def to_representation(self, device):
        # Get service instances where device is directly assigned OR device's role is assigned
        if not isinstance(device, Device) or not device.role:
            service_instances = NSOServiceInstance.objects.filter(devices=device)
        else:
            service_instances = NSOServiceInstance.objects.filter(
                Q(devices=device) | Q(device_roles=device.role)
            ).distinct()

        # Serialize the instances
        serializer = NestedNSOServiceInstanceSerializer(service_instances, many=True, context=self.context)
        return serializer.data


# This function will be called by NetBox to extend the Device API serializer
def extend_device_serializer(serializer_class):
    """Add nso_service_instances field to Device serializer"""

    class ExtendedDeviceSerializer(serializer_class):
        nso_service_instances = DeviceNSOServicesField(read_only=True)

        class Meta(serializer_class.Meta):
            fields = serializer_class.Meta.fields + ['nso_service_instances']

    return ExtendedDeviceSerializer
