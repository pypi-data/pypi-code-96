# Generated by Django 3.2.3 on 2021-06-03 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0046_cities_region'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City_regions',
        ),
    ]
