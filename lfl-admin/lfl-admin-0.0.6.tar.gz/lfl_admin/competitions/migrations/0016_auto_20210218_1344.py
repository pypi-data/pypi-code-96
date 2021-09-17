# Generated by Django 3.1.6 on 2021-02-18 13:44

import bitfield.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_region_text_informations_code'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0015_tournament_types_tournaments'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournaments',
            name='division_priority',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='modified_by',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='number_of_players',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='number_of_rounds',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='number_of_teams',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='number_of_tours',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='priority',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='props',
            field=bitfield.models.BitField((('active', 'active'), ('national', 'national'), ('show_league', 'show_league'), ('show_region', 'show_region'), ('up_selected', 'up_selected'), ('up2_selected', 'up2_selected'), ('down_selected', 'down_selected'), ('down_selected', 'down2_selected'), ('calendar_created', 'calendar_created'), ('show_numbers', 'show_numbers')), db_index=True, default=1),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='rating_rule',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='start_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='technical_defeat',
            field=models.CharField(default='5:0', max_length=5),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='type',
            field=isc_common.fields.related.ForeignKeyProtect(default=None, on_delete=django.db.models.deletion.PROTECT, to='competitions.tournament_types'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='league',
            field=isc_common.fields.related.ForeignKeyProtect(default=None, on_delete=django.db.models.deletion.PROTECT, to='competitions.leagues'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='region',
            field=isc_common.fields.related.ForeignKeyProtect(default=None, on_delete=django.db.models.deletion.PROTECT, to='region.regions'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='round',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='seasson',
            field=isc_common.fields.related.ForeignKeyProtect(default=None, on_delete=django.db.models.deletion.PROTECT, to='competitions.seassons'),
        ),
    ]
