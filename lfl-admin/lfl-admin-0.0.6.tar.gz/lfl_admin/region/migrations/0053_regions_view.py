# Generated by Django 3.2.4 on 2021-06-08 09:22

import bitfield.models
from django.db import migrations, models
import django.utils.timezone
import isc_common.fields.code_field
import isc_common.fields.description_field
import isc_common.fields.name_field


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0052_auto_20210606_0734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regions_view',
            fields=[
                ('old_id', models.BigIntegerField(blank=True, db_index=True, null=True, unique=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('code', isc_common.fields.code_field.CodeStrictField()),
                ('name', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('description', isc_common.fields.description_field.DescriptionField()),
                ('active', models.BooleanField()),
                ('contacts', models.TextField(blank=True, null=True)),
                ('logo_image_src', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('logo_real_name', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('header_image_src', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('header_real_name', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('props', bitfield.models.BitField((('active', 'Актуальность'), ('select_division', 'select_division'), ('parimatch', 'parimatch'), ('submenu', 'submenu'), ('leagues_menu', 'leagues_menu')), db_index=True, default=1)),
            ],
            options={
                'verbose_name': 'Регионы',
                'db_table': 'region_region_view',
                'managed': False,
            },
        ),
    ]
