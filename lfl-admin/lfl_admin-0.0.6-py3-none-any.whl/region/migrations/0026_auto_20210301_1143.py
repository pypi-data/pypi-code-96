# Generated by Django 3.1.6 on 2021-03-01 11:43

import django.db.models.deletion
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_auto_20210301_1105'),
        ('isc_common', '0074_auto_20210301_1105'),
        ('region', '0025_auto_20210301_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='region_zone_phones',
            name='zone',
            field=isc_common.fields.related.ForeignKeyProtect(default=None, on_delete=django.db.models.deletion.PROTECT, to='region.region_zones'),
        ),
        migrations.AlterUniqueTogether(
            name='region_zone_images',
            unique_together={('zone', 'image')},
        ),
        migrations.AlterUniqueTogether(
            name='region_zone_phones',
            unique_together={('zone', 'phone')},
        ),
        migrations.RemoveField(
            model_name='region_zone_phones',
            name='image',
        ),
    ]
