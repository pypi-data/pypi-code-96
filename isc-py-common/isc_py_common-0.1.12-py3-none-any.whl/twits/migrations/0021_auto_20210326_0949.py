# Generated by Django 3.1.7 on 2021-03-26 09:49

from django.db import migrations

import isc_common.fields.code_field


class Migration(migrations.Migration):
    dependencies = [
        ('twits', '0020_auto_20210326_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='code',
            field=isc_common.fields.code_field.CodeStrictField(unique=True),
        ),
    ]
