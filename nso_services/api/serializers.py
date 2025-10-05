from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox.api.serializers import WritableNestedSerializer
from dcim.models import Device, DeviceRole
from nso_services.models import NSOService, NSOServiceInstance


class NestedDeviceSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='dcim-api:device-detail')

    class Meta:
        model = Device
        fields = ['id', 'url', 'display', 'name']


class NestedDeviceRoleSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='dcim-api:devicerole-detail')

    class Meta:
        model = DeviceRole
        fields = ['id', 'url', 'display', 'name']


class NestedNSOServiceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:nso_services-api:nsoservice-detail')

    class Meta:
        model = NSOService
        fields = ['id', 'url', 'display', 'name']
        brief_fields = ['id', 'url', 'display', 'name']


class NestedNSOServiceInstanceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:nso_services-api:nsoserviceinstance-detail')

    class Meta:
        model = NSOServiceInstance
        fields = ['id', 'url', 'display', 'name']
        brief_fields = ['id', 'url', 'display', 'name']


class NSOServiceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:nso_services-api:nsoservice-detail')
    instances = NestedNSOServiceInstanceSerializer(many=True, read_only=True, source='nso_instances')

    class Meta:
        model = NSOService
        fields = ['id', 'url', 'display', 'name', 'status', 'region', 'git_repo_url', 'description', 'json_body', 'instances', 'comments', 'tags', 'custom_fields', 'created', 'last_updated']


class DeviceRoleWithDevicesSerializer(NestedDeviceRoleSerializer):
    """Extended device role serializer that includes devices with that role"""
    in_role_devices = serializers.SerializerMethodField()

    class Meta(NestedDeviceRoleSerializer.Meta):
        fields = NestedDeviceRoleSerializer.Meta.fields + ['in_role_devices']

    def get_in_role_devices(self, obj):
        """Get all devices with this role"""
        return NestedDeviceSerializer(obj.devices.all(), many=True, context=self.context).data


class NSOServiceInstanceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:nso_services-api:nsoserviceinstance-detail')
    service = NestedNSOServiceSerializer(read_only=True)
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=NSOService.objects.all(),
        source='service',
        write_only=True
    )
    direct_devices = NestedDeviceSerializer(many=True, read_only=True, source='devices')
    direct_device_ids = serializers.PrimaryKeyRelatedField(
        queryset=Device.objects.all(),
        many=True,
        source='devices',
        write_only=True,
        required=False
    )
    device_roles = DeviceRoleWithDevicesSerializer(many=True, read_only=True)
    device_role_ids = serializers.PrimaryKeyRelatedField(
        queryset=DeviceRole.objects.all(),
        many=True,
        source='device_roles',
        write_only=True,
        required=False
    )
    overlapping_devices = serializers.SerializerMethodField()

    class Meta:
        model = NSOServiceInstance
        fields = ['id', 'url', 'display', 'service', 'service_id', 'name', 'status', 'region', 'direct_devices', 'direct_device_ids', 'device_roles', 'device_role_ids', 'overlapping_devices', 'json_body', 'comments', 'tags', 'custom_fields', 'created', 'last_updated']
        brief_fields = ['id', 'url', 'display', 'name']

    def get_overlapping_devices(self, obj):
        """Get devices that are assigned both directly and via device role"""
        directly_assigned = set(obj.devices.all())
        devices_via_roles = set()

        for role in obj.device_roles.all():
            devices_via_roles.update(role.devices.all())

        overlap = directly_assigned & devices_via_roles

        if overlap:
            return {
                'warning': 'Some devices are assigned both directly and via device role',
                'devices': NestedDeviceSerializer(list(overlap), many=True, context=self.context).data
            }
        return None