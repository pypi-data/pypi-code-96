# Generated by Django 2.2.9 on 2020-02-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_data_manager", "0014_auto_20191213_0314"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalqueryrule",
            name="rule_handler_name",
            field=models.CharField(
                choices=[
                    ("do_nothing", "Do Nothing"),
                    ("default", "Default"),
                    ("lumbar_puncture_q13", "Lumbar Puncture (Q13, 15, 21, 23, 24)"),
                ],
                default="default",
                max_length=150,
            ),
        ),
        migrations.AlterField(
            model_name="queryrule",
            name="rule_handler_name",
            field=models.CharField(
                choices=[
                    ("do_nothing", "Do Nothing"),
                    ("default", "Default"),
                    ("lumbar_puncture_q13", "Lumbar Puncture (Q13, 15, 21, 23, 24)"),
                ],
                default="default",
                max_length=150,
            ),
        ),
    ]
