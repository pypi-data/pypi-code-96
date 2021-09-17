# Generated by Django 3.2.6 on 2021-08-25 11:26

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0059_auto_20210823_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='region.cities'),
        ),
        migrations.AlterField(
            model_name='region_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='region.regions'),
        ),
        migrations.AlterField(
            model_name='region_zone_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='region.region_zones'),
        ),
    ]
