from django.db import models
from netbox.models import PrimaryModel
from dcim.models import Device, Region, DeviceRole
from dcim.choices import DeviceStatusChoices

class NSOService(PrimaryModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=50,
        choices=DeviceStatusChoices,
        default=DeviceStatusChoices.STATUS_ACTIVE
    )
    region = models.ForeignKey(
        to=Region,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='nso_services'
    )
    git_repo_url = models.URLField(
        max_length=500,
        blank=True,
        verbose_name='Git Repository URL',
        help_text='URL to the Git repository for this service'
    )
    json_body = models.JSONField(
        blank=True,
        null=True,
        verbose_name='JSON Body',
        help_text='JSON data for this service'
    )

    class Meta:
        verbose_name = "NSO Service"
        verbose_name_plural = "NSO Services"

    def __str__(self):
        return self.name

    def get_status_color(self):
        return DeviceStatusChoices.colors.get(self.status)

class NSOServiceInstance(PrimaryModel):
    service = models.ForeignKey(NSOService, on_delete=models.CASCADE, related_name='nso_instances')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=50,
        choices=DeviceStatusChoices,
        default=DeviceStatusChoices.STATUS_ACTIVE
    )
    region = models.ForeignKey(
        to=Region,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='nso_service_instances'
    )
    devices = models.ManyToManyField(Device, blank=True, related_name='nso_service_instances')
    device_roles = models.ManyToManyField(
        DeviceRole,
        blank=True,
        related_name='nso_service_instances',
        verbose_name='Device Roles',
        help_text='Device roles that should use this service instance'
    )
    json_body = models.JSONField(
        blank=True,
        null=True,
        verbose_name='JSON Body',
        help_text='JSON data for this service instance'
    )

    class Meta:
        verbose_name = "NSO Service Instance"
        verbose_name_plural = "NSO Service Instances"

    def __str__(self):
        return f"{self.name} ({self.service.name})"

    def get_status_color(self):
        return DeviceStatusChoices.colors.get(self.status)