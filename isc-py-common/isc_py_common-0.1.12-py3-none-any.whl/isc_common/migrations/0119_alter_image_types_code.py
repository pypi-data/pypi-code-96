# Generated by Django 3.2.6 on 2021-08-23 18:36

from django.db import migrations

import isc_common.fields.code_field


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0118_rename_keyimage_image_types_keyimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_types',
            name='code',
            field=isc_common.fields.code_field.CodeField(blank=True, null=True),
        ),
    ]
