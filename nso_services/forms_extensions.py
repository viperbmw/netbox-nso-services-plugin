from django import forms
from utilities.forms.fields import DynamicModelMultipleChoiceField
from netbox.forms import NetBoxModelForm
from dcim.models import Device
from .models import NSOServiceInstance

class DeviceNSOServiceInstancesForm(NetBoxModelForm):
    """
    Form extension to add NSO Service Instances field to Device form
    """
    nso_service_instances = DynamicModelMultipleChoiceField(
        queryset=NSOServiceInstance.objects.all(),
        required=False,
        label='NSO Service Instances',
        help_text='Assign this device to NSO service instances',
        query_params={}
    )

    class Meta:
        model = Device
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            # Pre-populate with currently assigned service instances
            self.initial['nso_service_instances'] = NSOServiceInstance.objects.filter(
                devices=self.instance
            )

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)

        if self.cleaned_data.get('nso_service_instances') is not None:
            # Get current service instances
            current_instances = set(NSOServiceInstance.objects.filter(devices=instance))
            # Get selected service instances
            selected_instances = set(self.cleaned_data['nso_service_instances'])

            # Add device to new service instances
            for service_instance in selected_instances - current_instances:
                service_instance.devices.add(instance)

            # Remove device from unselected service instances
            for service_instance in current_instances - selected_instances:
                service_instance.devices.remove(instance)

        return instance
