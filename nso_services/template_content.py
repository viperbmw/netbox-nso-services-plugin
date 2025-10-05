from netbox.plugins import PluginTemplateExtension
from django.db.models import Q
from dcim.models import Device, DeviceRole
from .models import NSOServiceInstance

class DeviceNSOServices(PluginTemplateExtension):
    model = 'dcim.device'

    def right_page(self):
        # Only show if the object is actually a Device instance
        obj = self.context['object']
        if not isinstance(obj, Device):
            return ''

        # Get service instances where:
        # 1. Device is directly assigned, OR
        # 2. Device's role is assigned
        service_instances = NSOServiceInstance.objects.filter(
            Q(devices=obj) | Q(device_roles=obj.role)
        ).distinct()

        return self.render('nso_services/device_service_instances.html', extra_context={
            'service_instances': service_instances
        })

class DeviceRoleNSOServices(PluginTemplateExtension):
    model = 'dcim.devicerole'

    def right_page(self):
        # Only show if the object is actually a DeviceRole instance
        obj = self.context['object']
        if not isinstance(obj, DeviceRole):
            return ''

        # Get service instances assigned to this device role
        service_instances = NSOServiceInstance.objects.filter(
            device_roles=obj
        ).distinct()

        return self.render('nso_services/devicerole_service_instances.html', extra_context={
            'service_instances': service_instances
        })

template_extensions = [DeviceNSOServices, DeviceRoleNSOServices]