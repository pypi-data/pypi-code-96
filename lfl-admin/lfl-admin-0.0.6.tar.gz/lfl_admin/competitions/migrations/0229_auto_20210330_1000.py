# Generated by Django 3.1.7 on 2021-03-30 10:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('competitions', '0228_auto_20210330_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disqualifications',
            name='from_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
