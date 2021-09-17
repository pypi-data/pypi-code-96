# Generated by Django 3.2.4 on 2021-06-18 06:27

import django.db.models.deletion
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):
    dependencies = [
        ('statistic', '0013_auto_20210618_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiting_of_players_division',
            name='raiting',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='statistic.raiting_of_players'),
        ),
        migrations.AlterField(
            model_name='raiting_of_players_tournamet',
            name='raiting',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='statistic.raiting_of_players'),
        ),
    ]
