# Generated by Django 3.2.3 on 2021-06-03 10:41

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0275_tournament_member_doubles_old_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasons',
            name='props',
            field=bitfield.models.BitField((('active', 'active'),), db_index=True, default=0),
        ),
    ]
