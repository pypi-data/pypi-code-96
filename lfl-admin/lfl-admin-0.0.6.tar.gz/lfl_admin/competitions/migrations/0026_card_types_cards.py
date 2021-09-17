# Generated by Django 3.1.6 on 2021-02-18 15:39

import bitfield.models
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import isc_common.fields.code_field
import isc_common.fields.description_field
import isc_common.fields.name_field
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('isc_common', '0066_auditmodelex'),
        ('competitions', '0025_disqualification_types_disqualifications_disqualifications_text_informations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card_types',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('code', isc_common.fields.code_field.CodeField(blank=True, null=True)),
                ('name', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('description', isc_common.fields.description_field.DescriptionField()),
            ],
            options={
                'verbose_name': 'Тип карточки',
            },
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('auditmodelex_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='isc_common.auditmodelex')),
                ('minute', models.SmallIntegerField()),
                ('props', bitfield.models.BitField((('take_off', 'take_off'),), db_index=True, default=1)),
                ('card_type', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.card_types')),
                ('club', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.clubs')),
                ('match', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.matches')),
                ('player', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.players')),
                ('referee', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('tournament', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.tournaments')),
            ],
            options={
                'verbose_name': 'Карточки игроков в сыгранных матчах: три типа. 1. жёлтая к. 2. Вторая ж.к. 3. красная карточка',
            },
            bases=('isc_common.auditmodelex',),
        ),
    ]
