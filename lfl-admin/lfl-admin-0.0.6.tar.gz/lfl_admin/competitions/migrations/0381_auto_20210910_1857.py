# Generated by Django 3.2.7 on 2021-09-10 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0380_match_stats_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match_stats',
            name='stat_key',
        ),
        migrations.RemoveField(
            model_name='match_stats',
            name='stat_title',
        ),
    ]
