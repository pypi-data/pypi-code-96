# Generated by Django 3.2.6 on 2021-08-09 15:55

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('react', '0013_page_level_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='type',
            field=isc_common.fields.related.ForeignKeyProtect(default=None, on_delete=django.db.models.deletion.PROTECT, to='react.page_level_types'),
            preserve_default=False,
        ),
    ]
