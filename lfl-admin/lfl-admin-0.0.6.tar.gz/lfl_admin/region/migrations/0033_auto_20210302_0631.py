# Generated by Django 3.1.6 on 2021-03-02 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0032_auto_20210302_0627'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='region_images',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='region_zone_images',
            unique_together=set(),
        ),
    ]
