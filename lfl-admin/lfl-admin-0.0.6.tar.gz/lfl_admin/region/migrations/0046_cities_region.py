# Generated by Django 3.2.3 on 2021-06-03 12:27

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0045_auto_20210603_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='region',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='region.regions'),
        ),
    ]
