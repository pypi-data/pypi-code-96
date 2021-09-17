# Generated by Django 3.1.7 on 2021-03-04 15:00

import django.db.models.deletion
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0085_divisions_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divisions',
            name='zone',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='competitions.disqualification_zones'),
        ),
    ]
