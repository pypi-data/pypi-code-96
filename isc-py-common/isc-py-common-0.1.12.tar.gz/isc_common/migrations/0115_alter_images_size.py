# Generated by Django 3.2.6 on 2021-08-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0114_auto_20210823_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='size',
            field=models.BigIntegerField(default=None, verbose_name='Размер файла'),
        ),
    ]
