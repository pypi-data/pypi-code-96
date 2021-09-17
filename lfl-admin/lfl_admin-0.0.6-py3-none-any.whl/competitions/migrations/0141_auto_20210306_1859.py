# Generated by Django 3.1.7 on 2021-03-06 18:59

import django.db.models.deletion
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0140_auto_20210306_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament_member_doubles',
            name='club_double',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Tournament_member_club_double', to='competitions.clubs'),
        ),
    ]
