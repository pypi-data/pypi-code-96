# Generated by Django 3.1.7 on 2021-03-10 05:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0159_auto_20210309_0954'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='players_change_history',
            unique_together={('date', 'editor', 'player')},
        ),
    ]
