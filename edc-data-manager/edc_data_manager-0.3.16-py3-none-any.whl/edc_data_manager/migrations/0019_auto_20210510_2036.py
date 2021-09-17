# Generated by Django 3.2 on 2021-05-10 17:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_data_manager', '0018_auto_20210203_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataquery',
            name='visit_code_sequence',
            field=models.IntegerField(blank=True, default=0, help_text="Defaults to '0'. For example, when combined with the visit code `1000` would make `1000.0`.", null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25)], verbose_name='Visit code sequence'),
        ),
        migrations.AlterField(
            model_name='historicaldataquery',
            name='visit_code_sequence',
            field=models.IntegerField(blank=True, default=0, help_text="Defaults to '0'. For example, when combined with the visit code `1000` would make `1000.0`.", null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25)], verbose_name='Visit code sequence'),
        ),
    ]
