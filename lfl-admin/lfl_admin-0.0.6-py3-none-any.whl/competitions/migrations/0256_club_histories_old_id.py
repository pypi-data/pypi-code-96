# Generated by Django 3.2 on 2021-04-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('competitions', '0255_auto_20210411_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='club_histories',
            name='old_id',
            field=models.BigIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
    ]
