from django.db import migrations, models
import dcim.choices


class Migration(migrations.Migration):

    dependencies = [
        ('nso_services', '0006_add_instance_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='nsoservice',
            name='status',
            field=models.CharField(choices=dcim.choices.DeviceStatusChoices, default='active', max_length=50),
        ),
        migrations.AddField(
            model_name='nsoserviceinstance',
            name='status',
            field=models.CharField(choices=dcim.choices.DeviceStatusChoices, default='active', max_length=50),
        ),
    ]
