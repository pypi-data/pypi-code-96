# Generated by Django 3.1.6 on 2021-03-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0008_auto_20210302_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='fields',
            name='old_id',
            field=models.BigIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='stadiums',
            name='old_id',
            field=models.BigIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
    ]
