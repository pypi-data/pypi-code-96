# Generated by Django 3.1.6 on 2021-02-18 12:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0009_club_histories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
            ],
            options={
                'verbose_name': 'Игроки',
            },
        ),
    ]
