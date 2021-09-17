# Generated by Django 3.2.6 on 2021-08-20 05:03

from django.db import migrations, models
import django.utils.timezone
import isc_common.fields.code_field
import isc_common.fields.description_field
import isc_common.fields.name_field


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0330_auto_20210819_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division_stages',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('code', isc_common.fields.code_field.CodeStrictField(unique=True)),
                ('name', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('description', isc_common.fields.description_field.DescriptionField()),
            ],
            options={
                'verbose_name': 'Эапы супертурнира',
            },
        ),
        migrations.AlterModelOptions(
            name='protocol_types',
            options={'verbose_name': 'Вариант протокола'},
        ),
    ]
