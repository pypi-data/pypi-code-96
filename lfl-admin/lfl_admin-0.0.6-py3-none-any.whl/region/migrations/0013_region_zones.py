# Generated by Django 3.1.6 on 2021-03-01 07:25

import django.utils.timezone
from django.db import migrations, models

import isc_common.fields.code_field
import isc_common.fields.description_field
import isc_common.fields.name_field
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0012_city_regions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region_zones',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('code', isc_common.fields.code_field.CodeField(blank=True, null=True)),
                ('name', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('description', isc_common.fields.description_field.DescriptionField()),
                ('parent', isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='region.region_zones')),
            ],
            options={
                'verbose_name': 'Зоны регионов',
            },
        ),
    ]
