# Generated by Django 3.2.4 on 2021-06-04 09:25

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0049_auto_20210604_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='region_zones',
            name='props',
            field=bitfield.models.BitField((('active', 'Заблокирован'),), db_index=True, default=0),
        ),
    ]
