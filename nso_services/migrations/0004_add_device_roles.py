# Add device_roles field to NSOServiceInstance

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nso_services', '0003_add_region_and_git_repo'),
        ('dcim', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='nsoserviceinstance',
            name='device_roles',
            field=models.ManyToManyField(
                blank=True,
                help_text='Device roles that should use this service instance',
                related_name='nso_service_instances',
                to='dcim.devicerole',
                verbose_name='Device Roles'
            ),
        ),
    ]
