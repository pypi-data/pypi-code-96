# Generated by Django 3.1.6 on 2021-02-19 09:16

from django.db import migrations, models

import isc_common.fields.files
import isc_common.fields.name_field


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0067_remove_auditmodelex_edited_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='attfile',
            field=isc_common.fields.files.FileFieldEx(blank=True, max_length=255, null=True, upload_to='', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='user',
            name='mime_type',
            field=isc_common.fields.name_field.NameField(blank=True, null=True, verbose_name='MIME тип файла файла'),
        ),
        migrations.AlterField(
            model_name='user',
            name='real_name',
            field=models.TextField(blank=True, null=True, verbose_name='Первоначальное имя файла'),
        ),
    ]
