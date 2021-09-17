# Generated by Django 3.1.6 on 2021-03-02 16:49

from django.db import migrations

import isc_common.fields.code_field


class Migration(migrations.Migration):

    dependencies = [
        ('user_ext', '0019_persons_persons_e_mails_persons_phones'),
    ]

    operations = [
        migrations.AddField(
            model_name='persons_e_mails',
            name='code',
            field=isc_common.fields.code_field.CodeStrictField(),
        ),
        migrations.AddField(
            model_name='persons_phones',
            name='code',
            field=isc_common.fields.code_field.CodeStrictField(),
        ),
    ]
