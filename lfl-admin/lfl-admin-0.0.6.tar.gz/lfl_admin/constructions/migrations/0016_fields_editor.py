# Generated by Django 3.1.7 on 2021-03-10 11:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('constructions', '0015_auto_20210309_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='fields',
            name='editor',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
