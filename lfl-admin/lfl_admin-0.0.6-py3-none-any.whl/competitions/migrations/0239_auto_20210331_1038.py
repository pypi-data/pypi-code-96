# Generated by Django 3.1.7 on 2021-03-31 10:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0238_auto_20210331_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='referees',
            name='creator',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='AuditModelEx_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='referees',
            name='editor',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='AuditModelEx_editor', to=settings.AUTH_USER_MODEL),
        ),
    ]
