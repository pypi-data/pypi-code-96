# Generated by Django 3.1.7 on 2021-03-06 13:38

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0108_auto_20210306_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournaments',
            name='props',
            field=bitfield.models.BitField((('active', 'active'), ('national', 'national'), ('show_league', 'show_league'), ('show_region', 'show_region'), ('up_selected', 'up_selected'), ('up2_selected', 'up2_selected'), ('down_selected', 'down_selected'), ('down2_selected', 'down2_selected'), ('calendar_created', 'calendar_created'), ('show_numbers', 'show_numbers'), ('show_player_number', 'show_player_number'), ('show_stats', 'show_stats'), ('show_empty_cells', 'show_empty_cells')), db_index=True, default=1),
        ),
    ]
