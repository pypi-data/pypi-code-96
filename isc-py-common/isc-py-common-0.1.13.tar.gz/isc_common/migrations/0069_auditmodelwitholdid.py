# Generated by Django 3.1.6 on 2021-02-20 05:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0068_auto_20210219_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditModelWithOldId',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('old_id', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
