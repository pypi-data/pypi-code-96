# Generated by Django 3.1.7 on 2021-03-06 13:52

import django.db.models.deletion
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0114_auto_20210306_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournaments',
            name='division',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.divisions'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='statistics_type',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.statistics_types'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='tournament_type',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.tournament_types'),
        ),
    ]
