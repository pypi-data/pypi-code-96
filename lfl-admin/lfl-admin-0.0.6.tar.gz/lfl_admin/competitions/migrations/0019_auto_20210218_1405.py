# Generated by Django 3.1.6 on 2021-02-18 14:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('region', '0011_region_text_informations_code'),
        ('competitions', '0018_tournament_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournaments',
            name='division_priority',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='league',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.leagues'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='modified_by',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='number_of_players',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='number_of_rounds',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='number_of_teams',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='number_of_tours',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='priority',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='rating_rule',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='region',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='region.regions'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='round',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='seasson',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.seassons'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='type',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.tournament_types'),
        ),
    ]
