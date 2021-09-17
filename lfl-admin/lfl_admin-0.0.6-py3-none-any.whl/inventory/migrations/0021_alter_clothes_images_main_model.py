# Generated by Django 3.2.6 on 2021-08-25 11:26

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0020_alter_clothes_images_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes_images',
            name='main_model',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='inventory.clothes'),
        ),
    ]
