# Generated by Django 3.2.6 on 2021-08-30 14:16

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0066_auto_20210830_1413'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='regions',
            name='c_cfdd491b_29bf_4112_b596_32c6b509fd07',
        ),
        migrations.AddConstraint(
            model_name='regions',
            constraint=models.CheckConstraint(check=models.Q(('id', django.db.models.expressions.F('parent_id')), _negated=True), name='c_region'),
        ),
    ]
