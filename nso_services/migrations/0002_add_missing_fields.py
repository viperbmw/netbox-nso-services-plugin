# Add missing PrimaryModel fields

from django.db import migrations, models
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ('nso_services', '0001_initial'),
    ]

    operations = [
        # Add missing fields to NSOService if they don't exist
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM information_schema.columns
                              WHERE table_name='nso_services_nsoservice' AND column_name='description') THEN
                    ALTER TABLE nso_services_nsoservice ADD COLUMN description text NOT NULL DEFAULT '';
                END IF;
                IF NOT EXISTS (SELECT 1 FROM information_schema.columns
                              WHERE table_name='nso_services_nsoservice' AND column_name='comments') THEN
                    ALTER TABLE nso_services_nsoservice ADD COLUMN comments text NOT NULL DEFAULT '';
                END IF;
                IF NOT EXISTS (SELECT 1 FROM information_schema.columns
                              WHERE table_name='nso_services_nsoservice' AND column_name='custom_field_data') THEN
                    ALTER TABLE nso_services_nsoservice ADD COLUMN custom_field_data jsonb NOT NULL DEFAULT '{}';
                END IF;
            END $$;
            """,
            reverse_sql="",
        ),
        # Add missing fields to NSOServiceInstance if they don't exist
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM information_schema.columns
                              WHERE table_name='nso_services_nsoserviceinstance' AND column_name='description') THEN
                    ALTER TABLE nso_services_nsoserviceinstance ADD COLUMN description text NOT NULL DEFAULT '';
                END IF;
                IF NOT EXISTS (SELECT 1 FROM information_schema.columns
                              WHERE table_name='nso_services_nsoserviceinstance' AND column_name='comments') THEN
                    ALTER TABLE nso_services_nsoserviceinstance ADD COLUMN comments text NOT NULL DEFAULT '';
                END IF;
                IF NOT EXISTS (SELECT 1 FROM information_schema.columns
                              WHERE table_name='nso_services_nsoserviceinstance' AND column_name='custom_field_data') THEN
                    ALTER TABLE nso_services_nsoserviceinstance ADD COLUMN custom_field_data jsonb NOT NULL DEFAULT '{}';
                END IF;
            END $$;
            """,
            reverse_sql="",
        ),
    ]
