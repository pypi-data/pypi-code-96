# Generated by Django 3.1.6 on 2021-02-19 08:40

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('votes', '0002_poll_answers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll_votes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('answer', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='votes.poll_answers')),
                ('author', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('poll', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='votes.polls')),
            ],
            options={
                'verbose_name': 'Подсчет голосов',
            },
        ),
    ]
