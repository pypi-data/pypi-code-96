# Generated by Django 3.1.7 on 2021-03-10 13:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('competitions', '0182_auto_20210310_1251'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='matchdays',
            unique_together={('tournament', 'tour')},
        ),
    ]
