# Generated by Django 3.2.7 on 2021-09-11 02:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0383_alter_match_stats_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referee_zone_view',
            fields=[
                ('old_id', models.BigIntegerField(blank=True, db_index=True, null=True, unique=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
            ],
            options={
                'verbose_name': ('Главные судьи в матчах',),
                'db_table': 'competitions_referee_zones_view',
                'managed': False,
            },
        ),
    ]
