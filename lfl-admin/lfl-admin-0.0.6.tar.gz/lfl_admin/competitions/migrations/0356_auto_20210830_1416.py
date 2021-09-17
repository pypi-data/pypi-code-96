# Generated by Django 3.2.6 on 2021-08-30 14:16

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0355_auto_20210830_1413'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='divisions',
            name='c_7c1d173b_3fc5_4e05_b35c_80b2fe47c96a',
        ),
        migrations.AddConstraint(
            model_name='divisions',
            constraint=models.CheckConstraint(check=models.Q(('id', django.db.models.expressions.F('parent_id')), _negated=True), name='c_Divisions'),
        ),
    ]
