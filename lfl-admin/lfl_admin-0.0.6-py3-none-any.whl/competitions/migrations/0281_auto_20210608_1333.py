# Generated by Django 3.2.4 on 2021-06-08 13:33

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0280_auto_20210608_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divisions',
            name='disqualification_condition',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.disqualification_condition'),
        ),
        migrations.AlterModelTable(
            name='divisions_view',
            table='competitions_divisions_view',
        ),
    ]
