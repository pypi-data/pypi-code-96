# Generated by Django 3.2.6 on 2021-08-29 13:47

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0351_alter_tournaments_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='competitions.calendar'),
        ),
        migrations.AlterField(
            model_name='club_logo_history_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='competitions.club_logo_history'),
        ),
        migrations.AlterField(
            model_name='clubs_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='competitions.clubs'),
        ),
        migrations.AlterField(
            model_name='divisions_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='competitions.divisions'),
        ),
        migrations.AlterField(
            model_name='leagues_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='competitions.leagues'),
        ),
        migrations.AlterField(
            model_name='players_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='competitions.players'),
        ),
        migrations.AlterField(
            model_name='referees_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='competitions.referees'),
        ),
        migrations.AlterField(
            model_name='tournaments_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='competitions.tournaments'),
        ),
    ]
