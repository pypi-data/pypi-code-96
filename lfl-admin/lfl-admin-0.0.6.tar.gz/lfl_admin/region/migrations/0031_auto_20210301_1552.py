# Generated by Django 3.1.6 on 2021-03-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0030_region_links_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='old_id',
            field=models.BigIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='region_zones',
            name='old_id',
            field=models.BigIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='regions',
            name='old_id',
            field=models.BigIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
    ]
