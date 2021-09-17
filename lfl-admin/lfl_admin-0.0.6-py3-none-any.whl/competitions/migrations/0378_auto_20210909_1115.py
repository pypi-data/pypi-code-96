# Generated by Django 3.2.7 on 2021-09-09 11:15

import bitfield.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0377_remove_players_size_of_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='height',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='props',
            field=bitfield.models.BitField((('active', 'active'), ('shadow', 'Скрыть данные игорока'), ('blocked', 'blocked'), ('disqualification', 'Дисквалифицирован'), ('lockout', 'Не допущен к играм'), ('delayed_lockout', 'Отложенный недопуск'), ('medical_lockout', 'medical_lockout')), db_index=True, default=1),
        ),
        migrations.AlterField(
            model_name='players',
            name='weight',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
