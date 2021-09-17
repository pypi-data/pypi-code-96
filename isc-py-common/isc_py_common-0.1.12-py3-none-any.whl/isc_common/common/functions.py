import logging
import re

from django.db import connection
from isc_common import setAttr
from isc_common.number import ToStr

logger = logging.getLogger(__name__)


def uncapitalize(str):
    return str[0:1].lower() + str[1:]


def dbl_qutes_str(str):
    return f'"{str}"'


def qutes_str(str):
    return f"'{str}'"


def delete_dbl_spaces(value):
    if value is None:
        return value

    if not isinstance(value, str):
        return ToStr(value)

    value = value.replace('\\n', ' ')
    return re.sub('\s+', ' ', value).strip()


def null2blanck(str):
    return '' if str == 'null' else str


def ExecuteStoredProc(storedProcName, parametrs):
    c = connection.cursor()
    try:
        # c.execute("BEGIN")
        res = c.callproc(storedProcName, parametrs)
        results, = c.fetchone()
        # c.execute("COMMIT")
        return results
    except Exception as ex:
        logger.error(ex)
        raise ex
    finally:
        c.close()


def ExecuteStoredProcRows(storedProcName, parametrs):
    c = connection.cursor()
    try:
        # c.execute("BEGIN")
        res = c.callproc(storedProcName, parametrs)
        results = c.fetchall()
        # c.execute("COMMIT")
        return results
    except Exception as ex:
        logger.error(ex)
        raise ex
    finally:
        c.close()


class Common:
    @classmethod
    def get_size_file_str(cls, value):
        if value == 0:
            return ""

        if value > 0 and value <= 1024:
            return f'{value} Байт'

        if value > 1024 and value <= 1024 * 1024:
            return f'{round(value / 1024, 2)} КБайт'

        if value > 1024 * 1024 and value <= 1024 * 1024 * 1024:
            return f'{round(value / 1024 / 1024, 2)} МБайт'

        if value > 1024 * 1024 * 1024:
            return f'{round(value / 1024 / 1024 / 1024, 2)}  ГБайт'
        return value

    @classmethod
    def arraund_error(error):
        str = '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        return f'\n{str}\n{error}\n{str}'


def get_fields_name_from_model(model, data):
    res = list(filter(lambda x: x != 'id' and data.get(x) is not None, map(lambda x: x.name, model._meta.fields)))
    res.extend(list(map(lambda x: f'{x.name}_id', filter(lambda x: x.is_relation is True and x.name not in res, model._meta.fields))))
    return res


def get_relation_field_name(model):
    res = list(map(lambda x: x.name, filter(lambda x: x.is_relation is True and x.name != 'parent', model._meta.fields)))
    return res


def get_dict_only_model_field(data, model, exclude=[]):
    res = dict()
    fields_name = get_fields_name_from_model(model, data)
    for k, v in data.items():
        if k in fields_name and not k in exclude:
            setAttr(res, k, v)
    return res


def check_image_files(apps, schema_editor):
    from isc_common.models.images import Images
    from tqdm import tqdm
    from isc_common.fields.files import make_REPLACE_IMAGE_PATH
    from django.conf import settings
    from lfl_admin.common.management.commands import update_img_refs
    from isc_common.fields.files import FILE_ex
    import os

    query = Images.objects.exclude().order_by('id')
    pbar = tqdm(total=query.count())
    ssh_files = settings.SSH_CLIENTS.client(settings.FILES_STORE)
    o_ssh_files = settings.SSH_CLIENTS.client( settings.OLD_FILES )

    for image in query:

        image_fullpath = make_REPLACE_IMAGE_PATH(image.real_name)
        deleted = False
        if o_ssh_files.exists(image_fullpath) is False:
            logger.debug(f'Deliting : {image}')
            try:
                if FILE_ex(image=image, ssh_files=ssh_files)[0] is False:
                    image.delete()
                    deleted = True
            except Exception as ex:
                deleted = True
                image.file_name = None
                image.size = 0
                image.attfile = ''
                image.save()
                logger.error(ex)

        if deleted is False:
            exists, size = FILE_ex(image=image, ssh_files=ssh_files)
            if exists is True:
                _, file_name = os.path.split(image_fullpath)
                imagen = Images.objects.exclude(id=image.id).getOptional(file_name=file_name, size=size)

                if imagen is not None:
                    update_img_refs(old_id=imagen.id, new_id=image.id)
                image.file_name = file_name
                image.size = size
                image.save()

            else:
                image.file_name = None
                image.size = 0
                image.attfile = ''
                image.save()

        pbar.update()
    logger.info('Done.')
