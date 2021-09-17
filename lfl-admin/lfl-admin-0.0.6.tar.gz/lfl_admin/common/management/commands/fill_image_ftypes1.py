import logging

from django.core.management import BaseCommand
from django.db import transaction, connection

from lfl_admin.common.models.all_tables import All_tables

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Установка правильных типов картиноц"

    def handle(self, *args, **options):
        i = 1
        with transaction.atomic():
            for table in All_tables.objects.filter(table_name__endswith='_images').exclude(table_name__in=['common_site_lfl_images', 'isc_common_images']).order_by('table_name'):
                # print(table.table_name)
                with connection.cursor() as cursor:
                    sql_str = f'''select id, code, keyimage
                                        from isc_common_image_types
                                        where id in (select distinct icit.id
                                                     from {table.table_name} as cli
                                                              join isc_common_image_types icit on cli.type_id = icit.id)'''

                    cursor.execute(sql_str)
                    rows = cursor.fetchall()
                    for row in rows:
                        id, code, keyimage = row

                        rindex = table.table_name.rfind('_')
                        index = table.table_name.find('_')
                        model = table.table_name[index + 1: rindex]

                        cursor.execute(f'''select count(*) from isc_common_image_types 
                                            where code=%s 
                                              and  keyimage=%s''', [model, code])
                        qnt, = cursor.fetchone()

                        if qnt == 0:
                            sql_str = f'''insert into isc_common_image_types (deleted_at, editing, deliting, lastmodified, code, name, description, parent_id, height, width, keyimage) 
                                          values(null, false, false, NOW(), %s , null, null, null, null,null, %s) returning id'''

                            cursor.execute(sql_str, [model, code])
                            new_id, = cursor.fetchone()

                            cursor.execute(f'update {table.table_name} set type_id = %s where type_id = %s', [new_id, id])

                        print(model, code, id)

            with connection.cursor() as cursor:
                cursor.execute('delete from isc_common_image_types where keyimage is null')
