# Generated by Django 3.2.6 on 2021-08-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('react', '0021_auto_20210811_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='fragment_params',
            name='num',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fragment_params',
            name='path_file',
            field=models.TextField(blank=True, null=True),
        ),
    ]
