# Generated by Django 3.2.4 on 2021-06-04 07:04

from django.db import migrations, models
import django.utils.timezone
import isc_common.fields.code_field
import isc_common.fields.description_field
import isc_common.fields.name_field


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0047_delete_city_regions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities_view',
            fields=[
                ('old_id', models.BigIntegerField(blank=True, db_index=True, null=True, unique=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('code', isc_common.fields.code_field.CodeStrictField(unique=True)),
                ('name', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('description', isc_common.fields.description_field.DescriptionField()),
                ('image_src', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('real_name', isc_common.fields.name_field.NameField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Города',
                'db_table': 'region_cities_view',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='cities',
            name='parent',
        ),
        migrations.AlterField(
            model_name='cities',
            name='code',
            field=isc_common.fields.code_field.CodeStrictField(unique=True),
        ),
    ]
