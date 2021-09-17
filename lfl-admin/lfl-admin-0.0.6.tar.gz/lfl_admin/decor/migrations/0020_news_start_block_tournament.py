# Generated by Django 3.1.7 on 2021-03-11 06:21

import bitfield.models
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import isc_common.fields.related


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0186_calendar_links'),
        ('decor', '0019_news_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_start_block_tournament',
            fields=[
                ('old_id', models.BigIntegerField(blank=True, db_index=True, null=True, unique=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('props', bitfield.models.BitField((('active', 'active'), ('disable_editor', 'disable_editor'), ('in_middle', 'in_middle'), ('in_top', 'in_top')), db_index=True, default=1)),
                ('admin', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, related_name='News_start_block_tournament_admin', to=settings.AUTH_USER_MODEL)),
                ('created', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, related_name='News_start_block_tournament_created', to=settings.AUTH_USER_MODEL)),
                ('tournament', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.tournaments')),
            ],
            options={
                'verbose_name': 'Новости, встраиваемые блоки, видео',
            },
        ),
    ]
