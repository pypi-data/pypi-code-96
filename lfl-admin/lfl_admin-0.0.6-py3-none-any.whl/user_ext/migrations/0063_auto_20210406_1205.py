# Generated by Django 3.1.7 on 2021-04-06 12:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_ext', '0062_auto_20210331_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='creator',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contacts',
            name='editor',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
