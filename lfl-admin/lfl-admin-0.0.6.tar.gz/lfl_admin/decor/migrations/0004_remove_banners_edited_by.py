# Generated by Django 3.1.6 on 2021-02-19 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('decor', '0003_menus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banners',
            name='edited_by',
        ),
    ]
