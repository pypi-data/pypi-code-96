# Generated by Django 3.2.4 on 2021-06-17 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0004_rename_stand_off_raiting_of_players_stand_off_cnt'),
    ]

    operations = [
        migrations.AddField(
            model_name='raiting_of_players',
            name='not_win_cnt',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, verbose_name='Ничьих'),
            preserve_default=False,
        ),
    ]
