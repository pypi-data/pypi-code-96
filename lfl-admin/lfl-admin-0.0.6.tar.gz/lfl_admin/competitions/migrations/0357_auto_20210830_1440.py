# Generated by Django 3.2.6 on 2021-08-30 14:40

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0356_auto_20210830_1416'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='clubs',
            constraint=models.CheckConstraint(check=models.Q(('id', django.db.models.expressions.F('parent_id')), _negated=True), name='c_Clubs'),
        ),
        migrations.AddConstraint(
            model_name='seasons',
            constraint=models.CheckConstraint(check=models.Q(('id', django.db.models.expressions.F('parent_id')), _negated=True), name='c_Seasons'),
        ),
    ]
