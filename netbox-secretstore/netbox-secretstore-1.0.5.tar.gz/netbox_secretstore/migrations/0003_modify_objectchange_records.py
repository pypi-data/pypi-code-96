# Generated by Django 3.2.5 on 2021-07-20 17:30

from django.db import migrations


def secrets_to_nbsecrets(apps, schema_editor):
    try:
        ObjectChange = apps.get_model('extras', 'ObjectChange')
        ContentType = apps.get_model('contenttypes', 'ContentType')

        ctsecret = ContentType.objects.get(app_label='secrets', model='secret')
        ctsecretrole = ContentType.objects.get(app_label='secrets', model='secretrole')
        ctuserkey = ContentType.objects.get(app_label='secrets', model='userkey')
        ctsessionkey = ContentType.objects.get(app_label='secrets', model='sessionkey')

        ctnbsecret = ContentType.objects.get(app_label='netbox_secretstore', model='secret')
        ctnbsecretrole = ContentType.objects.get(app_label='netbox_secretstore', model='secretrole')
        ctnbuserkey = ContentType.objects.get(app_label='netbox_secretstore', model='userkey')
        ctnbsessionkey = ContentType.objects.get(app_label='netbox_secretstore', model='sessionkey')

        ObjectChange.objects.filter(changed_object_type_id=ctsecret.id).update(changed_object_type_id=ctnbsecret.id)
        ObjectChange.objects.filter(changed_object_type_id=ctsecretrole.id).update(changed_object_type_id=ctnbsecretrole.id)
        ObjectChange.objects.filter(changed_object_type_id=ctsessionkey.id).update(changed_object_type_id=ctnbsessionkey.id)
        ObjectChange.objects.filter(changed_object_type_id=ctuserkey.id).update(changed_object_type_id=ctnbuserkey.id)
    except ContentType.DoesNotExist:
        pass


def nbsecrets_to_secrets(apps, schema_editor):
    try:

        ObjectChange = apps.get_model('extras', 'ObjectChange')
        ContentType = apps.get_model('contenttypes', 'ContentType')

        ctsecret = ContentType.objects.get(app_label='secrets', model='secret')
        ctsecretrole = ContentType.objects.get(app_label='secrets', model='secretrole')
        ctuserkey = ContentType.objects.get(app_label='secrets', model='userkey')
        ctsessionkey = ContentType.objects.get(app_label='secrets', model='sessionkey')

        ctnbsecret = ContentType.objects.get(app_label='netbox_secretstore', model='secret')
        ctnbsecretrole = ContentType.objects.get(app_label='netbox_secretstore', model='secretrole')
        ctnbuserkey = ContentType.objects.get(app_label='netbox_secretstore', model='userkey')
        ctnbsessionkey = ContentType.objects.get(app_label='netbox_secretstore', model='sessionkey')

        ObjectChange.objects.filter(changed_object_type_id=ctnbsecret.id).update(changed_object_type_id=ctsecret.id)
        ObjectChange.objects.filter(changed_object_type_id=ctnbsecretrole.id).update(changed_object_type_id=ctsecretrole.id)
        ObjectChange.objects.filter(changed_object_type_id=ctnbsessionkey.id).update(changed_object_type_id=ctsessionkey.id)
        ObjectChange.objects.filter(changed_object_type_id=ctnbuserkey.id).update(changed_object_type_id=ctuserkey.id)
    except ContentType.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_secretstore', '0002_rename_table'),
    ]

    operations = [
        migrations.RunPython(code=secrets_to_nbsecrets, reverse_code=nbsecrets_to_secrets)
    ]
