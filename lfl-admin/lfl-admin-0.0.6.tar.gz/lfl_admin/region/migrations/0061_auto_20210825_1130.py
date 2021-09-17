# Generated by Django 3.2.6 on 2021-08-25 11:30

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0060_auto_20210825_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='region.cities'),
        ),
        migrations.AlterField(
            model_name='region_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='region.regions'),
        ),
        migrations.AlterField(
            model_name='region_zone_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='region.region_zones'),
        ),
    ]
