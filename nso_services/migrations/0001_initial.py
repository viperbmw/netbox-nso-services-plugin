# Initial migration for nso_services plugin

from django.db import migrations, models
import django.db.models.deletion
import utilities.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '__first__'),
        ('extras', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='NSOService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('description', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'NSO Service',
                'verbose_name_plural': 'NSO Services',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NSOServiceInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('description', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('name', models.CharField(max_length=100)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nso_instances', to='nso_services.nsoservice')),
                ('devices', models.ManyToManyField(blank=True, related_name='nso_service_instances', to='dcim.device')),
            ],
            options={
                'verbose_name': 'NSO Service Instance',
                'verbose_name_plural': 'NSO Service Instances',
            },
            bases=(models.Model,),
        ),
    ]
