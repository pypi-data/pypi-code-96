# Generated by Django 3.1.6 on 2021-02-18 04:37

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_image_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image_type',
            field=isc_common.fields.related.ForeignKeyProtect(default=None, on_delete=django.db.models.deletion.PROTECT, to='common.image_types'),
        ),
    ]
