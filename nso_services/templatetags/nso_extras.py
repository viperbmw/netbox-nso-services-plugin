from django import template

register = template.Library()

@register.filter
def role_device_count(instance):
    """Calculate total number of devices from all assigned device roles"""
    total = 0
    for role in instance.device_roles.all():
        total += role.devices.count()
    return total

@register.filter
def total_device_count(instance):
    """Calculate total devices (direct + via roles)"""
    direct = instance.devices.count()
    via_roles = role_device_count(instance)
    return direct + via_roles
