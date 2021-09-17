# Generated by Django 3.2.6 on 2021-08-17 21:08

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0315_alter_player_histories_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divisions',
            name='props',
            field=bitfield.models.BitField((('active', 'active'), ('completed', 'completed'), ('show_news', 'show_news'), ('favorites', 'Избранные'), ('hidden', 'Скрывать ФИО')), db_index=True, default=1),
        ),
    ]
