# Generated by Django 3.2 on 2021-04-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('constructions', '0021_stadium_rating_old_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadium_zones',
            name='old_id',
            field=models.BigIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
    ]
