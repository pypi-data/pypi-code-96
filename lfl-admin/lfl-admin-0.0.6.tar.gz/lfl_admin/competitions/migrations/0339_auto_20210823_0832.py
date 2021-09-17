# Generated by Django 3.2.6 on 2021-08-23 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0107_alter_users_images_unique_together'),
        ('competitions', '0338_auto_20210823_0831'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='divisions_images',
            unique_together={('image', 'main_model', 'type', 'deleted_at')},
        ),
        migrations.AlterUniqueTogether(
            name='leagues_images',
            unique_together={('main_model', 'image', 'type', 'deleted_at')},
        ),
    ]
