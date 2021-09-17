# Generated by Django 2.2.3 on 2019-07-02 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0003_auto_20190514_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='priority',
            field=models.PositiveIntegerField(default=10, help_text='Priority (lower is better) for overlapping observations'),
        ),
    ]
