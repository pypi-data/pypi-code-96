# Generated by Django 3.1.7 on 2021-03-06 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0098_referee_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='referee_category',
            name='old_id',
            field=models.BigIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
    ]
