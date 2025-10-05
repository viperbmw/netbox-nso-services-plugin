from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0001_initial'),
        ('nso_services', '0005_add_json_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='nsoserviceinstance',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nso_service_instances', to='dcim.region'),
        ),
    ]
