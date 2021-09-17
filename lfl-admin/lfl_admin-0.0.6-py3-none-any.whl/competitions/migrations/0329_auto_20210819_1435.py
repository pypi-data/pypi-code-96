# Generated by Django 3.2.6 on 2021-08-19 14:35

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0328_auto_20210819_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournaments',
            name='loss_points_rule',
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='props',
            field=bitfield.models.BitField((('active', 'active'), ('national', 'national'), ('show_league', 'show_league'), ('show_region', 'show_region'), ('up_selected', 'up_selected'), ('up2_selected', 'up2_selected'), ('down_selected', 'down_selected'), ('down2_selected', 'down2_selected'), ('calendar_created', 'calendar_created'), ('show_numbers', 'show_numbers'), ('show_player_number', 'show_player_number'), ('show_stats', 'show_stats'), ('show_empty_cells', 'show_empty_cells'), ('favorites', 'Избранные'), ('hidden', 'Скрывать ФИО'), ('loss_points_rule', 'Подключить расстановку команд в текущей (не итоговой таблице), в случае равенства очков, по потерянным очкам')), db_index=True, default=1),
        ),
    ]
