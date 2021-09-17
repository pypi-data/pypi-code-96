# Generated by Django 3.1.7 on 2021-03-10 12:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0180_auto_20210310_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='keepers',
            name='editor',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='keepers',
            name='match',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='competitions.calendar'),
        ),
        migrations.AlterUniqueTogether(
            name='keepers',
            unique_together={('match', 'tournament', 'player')},
        ),
    ]
