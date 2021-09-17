# Generated by Django 3.1.7 on 2021-03-26 10:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('competitions', '0217_auto_20210326_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disqualification_zones',
            name='old_id',
        ),
        migrations.AddField(
            model_name='disqualification_zones',
            name='old_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), blank=True, null=True, size=None, unique=True),
        ),
    ]
