# Generated by Django 3.2.6 on 2021-08-23 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0117_rename_key_image_types_keyimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image_types',
            old_name='keyImage',
            new_name='keyimage',
        ),
    ]
