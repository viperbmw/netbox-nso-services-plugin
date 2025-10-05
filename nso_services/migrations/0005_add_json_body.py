from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nso_services', '0004_add_device_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='nsoserviceinstance',
            name='json_body',
            field=models.JSONField(blank=True, null=True, verbose_name='JSON Body', help_text='JSON data for this service instance'),
        ),
    ]
