# Generated by Django 3.2.6 on 2021-08-19 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0325_tournaments_rating_rule1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournaments',
            old_name='rating_rule',
            new_name='rating_rule2',
        ),
    ]
