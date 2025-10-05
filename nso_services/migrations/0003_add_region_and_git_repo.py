# Add region and git_repo_url fields

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nso_services', '0002_add_missing_fields'),
        ('dcim', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='nsoservice',
            name='region',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='nso_services',
                to='dcim.region'
            ),
        ),
        migrations.AddField(
            model_name='nsoservice',
            name='git_repo_url',
            field=models.URLField(
                blank=True,
                max_length=500,
                verbose_name='Git Repository URL'
            ),
        ),
    ]
