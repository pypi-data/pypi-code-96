# Generated by Django 3.2.6 on 2021-08-23 07:21

import django.db.models.deletion
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0106_auto_20210823_0721'),
        ('decor', '0026_auto_20210326_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_images',
            name='type',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='isc_common.image_types'),
        ),
    ]
