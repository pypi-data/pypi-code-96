# Generated by Django 3.2.6 on 2021-08-23 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0119_alter_image_types_code'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='image_types',
            unique_together={('code', 'keyimage')},
        ),
    ]
