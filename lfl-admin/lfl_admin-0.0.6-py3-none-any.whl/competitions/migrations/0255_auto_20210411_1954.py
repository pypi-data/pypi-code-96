# Generated by Django 3.2 on 2021-04-11 19:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('competitions', '0254_alter_club_contacts_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club_contacts',
            name='old_id',
        ),
        migrations.AddField(
            model_name='club_contacts',
            name='old_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), blank=True, null=True, size=None, unique=True),
        ),
    ]
