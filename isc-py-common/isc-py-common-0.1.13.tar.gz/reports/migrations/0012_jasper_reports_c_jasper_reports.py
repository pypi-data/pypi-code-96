# Generated by Django 3.2.6 on 2021-08-30 14:40

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_auto_20210326_0948'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='jasper_reports',
            constraint=models.CheckConstraint(check=models.Q(('id', django.db.models.expressions.F('parent_id')), _negated=True), name='c_Jasper_reports'),
        ),
    ]
