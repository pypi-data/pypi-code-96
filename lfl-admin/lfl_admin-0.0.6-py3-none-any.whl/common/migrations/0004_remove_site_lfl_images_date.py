# Generated by Django 3.1.6 on 2021-02-17 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20210217_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site_lfl_images',
            name='date',
        ),
    ]
