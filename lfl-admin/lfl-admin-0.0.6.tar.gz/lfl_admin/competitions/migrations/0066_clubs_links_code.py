# Generated by Django 3.1.7 on 2021-03-04 05:59

from django.db import migrations

import isc_common.fields.code_field


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0065_auto_20210304_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubs_links',
            name='code',
            field=isc_common.fields.code_field.CodeStrictField(),
        ),
    ]
