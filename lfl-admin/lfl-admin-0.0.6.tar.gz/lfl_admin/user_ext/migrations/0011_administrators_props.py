# Generated by Django 3.1.6 on 2021-02-19 10:04

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_ext', '0010_auto_20210219_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrators',
            name='props',
            field=bitfield.models.BitField((('relevant', 'Актуальность'), ('send_email', 'send_email'), ('kdk_fine_deleting', 'kdk_fine_deleting'), ('person_editing', 'person_editing'), ('all_news_access', 'all_news_access'), ('public_access', 'public_access'), ('transfer_right', 'transfer_right'), ('news', 'news'), ('documents', 'documents'), ('official', 'official'), ('video', 'video'), ('blocks', 'blocks'), ('upload', 'upload'), ('tournament_members', 'tournament_members')), db_index=True, default=1),
        ),
    ]
