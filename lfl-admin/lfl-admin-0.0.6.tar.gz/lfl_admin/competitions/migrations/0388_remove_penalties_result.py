# Generated by Django 3.2.7 on 2021-09-14 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0387_command_structure_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='penalties',
            name='result',
        ),
    ]
