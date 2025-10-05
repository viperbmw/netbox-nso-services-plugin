from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelMultipleChoiceField, CommentField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from dcim.models import Device, Region, DeviceRole
from .models import NSOService, NSOServiceInstance

class ServiceForm(NetBoxModelForm):
    region = DynamicModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        label='Region'
    )
    json_body = forms.JSONField(
        required=False,
        label='Example JSON Body',
        help_text='Example JSON structure for service instances',
        widget=forms.Textarea(attrs={'rows': 10, 'class': 'form-control font-monospace'})
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('name', 'status', 'region', 'git_repo_url', 'description', 'tags', name='Service Details'),
        FieldSet('json_body', name='Example JSON Body'),
    )

    class Meta:
        model = NSOService
        fields = ['name', 'status', 'region', 'git_repo_url', 'description', 'json_body', 'tags', 'comments']

class ServiceInstanceForm(NetBoxModelForm):
    service = forms.ModelChoiceField(
        queryset=NSOService.objects.all(),
        label='Service',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    region = DynamicModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        label='Region'
    )
    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False,
        label='Devices'
    )
    device_roles = DynamicModelMultipleChoiceField(
        queryset=DeviceRole.objects.all(),
        required=False,
        label='Device Roles',
        help_text='Device roles that should use this service instance'
    )
    json_body = forms.JSONField(
        required=False,
        label='Deployed JSON Body',
        help_text='Actual deployed JSON for this instance',
        widget=forms.Textarea(attrs={'rows': 10, 'class': 'form-control font-monospace'})
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('service', 'name', 'status', 'region', name='Basic Details'),
        FieldSet('devices', 'device_roles', name='Assignments'),
        FieldSet('json_body', name='Deployed JSON Body'),
        FieldSet('description', 'tags', name='Additional Details'),
    )

    class Meta:
        model = NSOServiceInstance
        fields = ['service', 'name', 'status', 'region', 'devices', 'device_roles', 'json_body', 'description', 'tags', 'comments']


class ServiceInstanceAllocationForm(forms.Form):
    """Form for allocating existing service instances to devices or device roles"""
    instance = DynamicModelChoiceField(
        queryset=NSOServiceInstance.objects.all(),
        required=True,
        label='Service Instance',
        help_text='Select an existing service instance to allocate'
    )
