# Generated by Django 3.1.7 on 2021-03-06 11:58

import bitfield.models
import django.utils.timezone
from django.db import migrations, models

import isc_common.fields.code_field
import isc_common.fields.description_field
import isc_common.fields.name_field
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0039_auto_20210302_1649'),
        ('competitions', '0097_auto_20210305_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referee_category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('code', isc_common.fields.code_field.CodeField(blank=True, null=True)),
                ('name', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('description', isc_common.fields.description_field.DescriptionField()),
                ('priority', models.SmallIntegerField()),
                ('props', bitfield.models.BitField((('active', 'active'),), db_index=True, default=1)),
                ('region', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='region.regions')),
            ],
            options={
                'verbose_name': 'Категории судей',
            },
        ),
    ]
