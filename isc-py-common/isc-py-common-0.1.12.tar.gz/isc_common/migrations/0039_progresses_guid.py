# Generated by Django 3.0.3 on 2020-02-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0038_auto_20200209_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='progresses',
            name='guid',
            field=models.UUIDField(default=None),
        ),
    ]
