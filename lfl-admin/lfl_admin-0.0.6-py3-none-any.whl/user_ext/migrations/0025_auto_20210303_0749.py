# Generated by Django 3.1.7 on 2021-03-03 07:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_ext', '0024_administrators_old_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='creator',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='persons',
            name='editor',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='editor', to=settings.AUTH_USER_MODEL),
        ),
    ]
