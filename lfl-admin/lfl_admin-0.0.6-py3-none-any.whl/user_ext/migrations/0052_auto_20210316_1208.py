# Generated by Django 3.1.7 on 2021-03-16 12:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user_ext', '0051_auto_20210315_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persons',
            name='old_id',
        ),
        migrations.AddField(
            model_name='persons',
            name='old_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), blank=True, null=True, size=None, unique=True),
        ),
    ]
