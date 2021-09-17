# Generated by Django 2.2.18 on 2021-03-23 06:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestgroups', '0014_auto_20210123_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestgroup',
            name='ipp_value',
            field=models.FloatField(help_text='A multiplier to the base priority of the Proposal for this RequestGroup and all child Requests. A value > 1.0 will raise the priority and debit the Proposal ipp_time_available upon submission. If a Request does not complete, the time debited for that Request is returned. A value < 1.0 will lower the priority and credit the ipp_time_available of the Proposal up to the ipp_limit on the successful completion of a Request. The value is generally set to 1.05. More information can be found <a href="https://lco.global/files/User_Documentation/the_new_priority_factor.pdf">here</a>.', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
