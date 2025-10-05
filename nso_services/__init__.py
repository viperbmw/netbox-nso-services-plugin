from netbox.plugins import PluginConfig

class NSOServicesConfig(PluginConfig):
    name = 'nso_services'
    verbose_name = 'NSO Services'
    description = 'Track Cisco NSO services within NetBox'
    version = '0.1'
    author = 'cwd'
    author_email = 'casey@cwdavis.net'
    base_url = 'nso-services'
    required_settings = []
    default_settings = {}
    template_extensions = 'template_content.template_extensions'

    def ready(self):
        super().ready()
        from . import api  # noqa
        # Register API serializer extensions
        from dcim.api.serializers import DeviceSerializer
        from .api_extensions import extend_device_serializer

        # Extend the Device serializer to include NSO service instances
        extended_serializer = extend_device_serializer(DeviceSerializer)
        # Replace the DeviceSerializer in the module
        import dcim.api.serializers
        dcim.api.serializers.DeviceSerializer = extended_serializer

config = NSOServicesConfig