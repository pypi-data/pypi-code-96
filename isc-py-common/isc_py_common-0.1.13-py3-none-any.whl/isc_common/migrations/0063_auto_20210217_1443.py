# Generated by Django 3.1.6 on 2021-02-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0062_auto_20210217_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255, verbose_name='пароль'),
        ),
    ]
