# Generated by Django 3.1.7 on 2021-03-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0121_auto_20210306_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament_members',
            name='position',
            field=models.SmallIntegerField(),
        ),
    ]
