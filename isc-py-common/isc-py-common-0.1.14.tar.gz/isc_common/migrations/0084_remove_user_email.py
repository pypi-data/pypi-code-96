# Generated by Django 3.1.7 on 2021-03-15 11:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('isc_common', '0083_remove_users_images_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
