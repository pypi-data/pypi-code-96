# Generated by Django 3.2.7 on 2021-09-16 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0132_alter_images_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usergroup_permission',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='usergroup_permission',
            name='usergroup',
        ),
        migrations.RemoveField(
            model_name='usergroup_permission',
            name='widget',
        ),
        migrations.RemoveField(
            model_name='widgets_trees',
            name='parent',
        ),
        migrations.AlterModelOptions(
            name='usergroup',
            options={'verbose_name': 'группа'},
        ),
        migrations.DeleteModel(
            name='User_Permission',
        ),
        migrations.DeleteModel(
            name='Usergroup_permission',
        ),
        migrations.DeleteModel(
            name='Widgets_trees',
        ),
    ]
