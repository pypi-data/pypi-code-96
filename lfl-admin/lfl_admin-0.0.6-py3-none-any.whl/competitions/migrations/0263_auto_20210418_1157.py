# Generated by Django 3.2 on 2021-04-18 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0262_auto_20210413_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match_resaults',
            name='code',
        ),
        migrations.RemoveField(
            model_name='match_resaults',
            name='description',
        ),
        migrations.RemoveField(
            model_name='match_resaults',
            name='name',
        ),
    ]
