# Generated by Django 2.2.7 on 2019-11-14 05:21

import edc_model_fields.fields.other_charfield
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("meta_ae", "0003_auto_20191102_0033"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deathreport",
            name="cause_of_death_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldeathreport",
            name="cause_of_death_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
    ]
