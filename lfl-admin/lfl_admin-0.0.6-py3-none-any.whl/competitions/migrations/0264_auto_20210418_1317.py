# Generated by Django 3.2 on 2021-04-18 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0263_auto_20210418_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match_stats',
            name='code',
        ),
        migrations.RemoveField(
            model_name='match_stats',
            name='description',
        ),
        migrations.RemoveField(
            model_name='match_stats',
            name='name',
        ),
    ]
