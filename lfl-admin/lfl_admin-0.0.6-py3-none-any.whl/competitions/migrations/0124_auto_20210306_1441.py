# Generated by Django 3.1.7 on 2021-03-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0123_auto_20210306_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournaments',
            name='division_priority',
            field=models.SmallIntegerField(default=None),
        ),
    ]
