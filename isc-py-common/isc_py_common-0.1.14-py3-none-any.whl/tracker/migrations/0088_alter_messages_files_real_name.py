# Generated by Django 3.2.3 on 2021-05-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0087_auto_20210326_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages_files',
            name='real_name',
            field=models.TextField(db_index=True, default=None, verbose_name='Первоначальное имя файла'),
            preserve_default=False,
        ),
    ]
