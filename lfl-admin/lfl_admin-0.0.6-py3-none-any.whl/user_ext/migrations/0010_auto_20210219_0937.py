# Generated by Django 3.1.6 on 2021-02-19 09:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0020_auto_20210219_0916'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_ext', '0009_auto_20210219_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrators',
            name='post',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='common.posts'),
        ),
        migrations.AlterField(
            model_name='administrators',
            name='user',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
