# Generated by Django 3.2 on 2021-04-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('isc_common', '0094_alter_debug_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_images',
            name='old_id',
            field=models.BigIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
    ]
