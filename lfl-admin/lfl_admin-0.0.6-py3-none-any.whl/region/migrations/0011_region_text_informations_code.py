# Generated by Django 3.1.6 on 2021-02-18 10:46

from django.db import migrations
import isc_common.fields.code_field


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0010_city_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='region_text_informations',
            name='code',
            field=isc_common.fields.code_field.CodeStrictField(),
        ),
    ]
