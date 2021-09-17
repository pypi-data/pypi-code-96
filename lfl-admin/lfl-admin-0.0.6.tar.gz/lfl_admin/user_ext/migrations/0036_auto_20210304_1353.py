# Generated by Django 3.1.7 on 2021-03-04 13:53

import django.db.models.deletion
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0083_auto_20210304_1300'),
        ('user_ext', '0035_auto_20210304_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='club',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.clubs'),
        ),
    ]
