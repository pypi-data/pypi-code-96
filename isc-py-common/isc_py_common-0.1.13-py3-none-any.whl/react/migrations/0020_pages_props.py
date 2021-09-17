# Generated by Django 3.2.6 on 2021-08-11 16:45

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('react', '0019_fragment_params_fragment'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='props',
            field=bitfield.models.BitField((('application', 'Приложение'),), db_index=True, default=1),
        ),
    ]
