# Generated by Django 2.1.7 on 2019-03-19 18:14

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestgroups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acquisitionconfig',
            name='extra_params',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Extra AcquisitionConfig parameters', verbose_name='extra parameters'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='extra_params',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Extra Configuration parameters', verbose_name='extra parameters'),
        ),
        migrations.AlterField(
            model_name='constraints',
            name='extra_params',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Extra Constraints parameters', verbose_name='extra parameters'),
        ),
        migrations.AlterField(
            model_name='guidingconfig',
            name='extra_params',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Extra GuidingConfig parameters', verbose_name='extra parameters'),
        ),
        migrations.AlterField(
            model_name='guidingconfig',
            name='optical_elements',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Optical Element specification for this GuidingConfig'),
        ),
        migrations.AlterField(
            model_name='instrumentconfig',
            name='extra_params',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Extra InstrumentConfig parameters', verbose_name='extra parameters'),
        ),
        migrations.AlterField(
            model_name='instrumentconfig',
            name='optical_elements',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Specification of optical elements used for this InstrumentConfig'),
        ),
        migrations.AlterField(
            model_name='target',
            name='extra_params',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Extra Target parameters', verbose_name='extra parameters'),
        ),
    ]
