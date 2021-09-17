# Generated by Django 3.1.6 on 2021-03-02 13:18

import django.db.models.deletion
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('decor', '0009_auto_20210302_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menus',
            name='menu_type',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='decor.menu_type'),
        ),
    ]
