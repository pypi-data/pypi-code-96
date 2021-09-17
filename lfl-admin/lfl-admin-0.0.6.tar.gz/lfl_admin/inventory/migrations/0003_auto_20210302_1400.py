# Generated by Django 3.1.6 on 2021-03-02 14:00

import bitfield.models
import django.utils.timezone
from django.db import migrations, models

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0022_auto_20210301_1433'),
        ('competitions', '0056_auto_20210302_0641'),
        ('inventory', '0002_auto_20210218_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothes_type',
            name='club',
        ),
        migrations.RemoveField(
            model_name='clothes_type',
            name='parent',
        ),
        migrations.AddField(
            model_name='clothes',
            name='clothes_type',
            field=isc_common.fields.related.ForeignKeyProtect(default=None, on_delete=django.db.models.deletion.PROTECT, to='inventory.clothes_type'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='club',
            field=isc_common.fields.related.ForeignKeyProtect(default=None, on_delete=django.db.models.deletion.PROTECT, to='competitions.clubs'),
        ),
        migrations.CreateModel(
            name='Clothes_images',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('props', bitfield.models.BitField((('active', 'Актуальность'),), db_index=True, default=1)),
                ('image', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='common.images')),
                ('main_model', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='inventory.clothes')),
            ],
            options={
                'verbose_name': 'Кросс таблица',
                'unique_together': {('main_model', 'image')},
            },
        ),
    ]
