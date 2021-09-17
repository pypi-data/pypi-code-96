# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2019 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#   Alvaro del Castillo San Felix <acs@bitergia.com>
#

import logging

from .enrich import Enrich, metadata
from ..elastic_mapping import Mapping as BaseMapping


logger = logging.getLogger(__name__)


NO_ANCESTOR_TITLE = "NO_TITLE"


class Mapping(BaseMapping):

    @staticmethod
    def get_elastic_mappings(es_major):
        """Get Elasticsearch mapping.

        :param es_major: major version of Elasticsearch, as string
        :returns:        dictionary with a key, 'items', with the mapping
        """

        mapping = """
        {
            "properties": {
                "title_analyzed": {
                  "type": "text",
                  "index": true
                }
           }
        } """

        return {"items": mapping}


class ConfluenceEnrich(Enrich):

    mapping = Mapping

    def get_field_author(self):
        return 'by'

    def get_identities(self, item):
        """ Return the identities from an item """

        field = self.get_field_author()
        yield self.get_sh_identity(item, field)

    def get_project_repository(self, eitem):
        return str(eitem['space'])

    def get_users_data(self, item):
        """ If user fields are inside the global item dict """
        if 'data' in item:
            users_data = item['data']['version']
        else:
            # the item is directly the data (kitsune answer)
            users_data = item
        return users_data

    def get_sh_identity(self, item, identity_field=None):
        identity = {}

        user = item  # by default a specific user dict is expected
        if isinstance(item, dict) and 'data' in item:
            user = item['data']['version'][identity_field]

        identity['username'] = user['username'] if 'username' in user else user.get('publicName', None)
        identity['email'] = user.get('email', None)
        identity['name'] = user.get('displayName', None)

        return identity

    @metadata
    def get_rich_item(self, item):
        eitem = {}

        self.copy_raw_fields(self.RAW_FIELDS_COPY, item, eitem)
        # The real data
        page = item['data']

        # data fields to copy
        copy_fields = ["type", "id", "status", "title", "content_url"]
        for f in copy_fields:
            if f in page:
                eitem[f] = page[f]
            else:
                eitem[f] = None
        # Fields which names are translated
        map_fields = {"title": "title_analyzed"}
        for fn in map_fields:
            eitem[map_fields[fn]] = page[fn]

        version = page['version']

        if 'username' in version['by']:
            eitem['author_name'] = version['by']['username']
        else:
            eitem['author_name'] = version['by']['displayName']

        eitem['message'] = None
        if 'message' in version:
            eitem['message'] = version['message']
        eitem['version'] = version['number']
        eitem['date'] = version['when']
        eitem['url'] = page['_links']['base'] + page['_links']['webui']

        if '_expandable' in page and 'space' in page['_expandable']:
            eitem['space'] = page['_expandable']['space']
            eitem['space'] = eitem['space'].replace('/rest/api/space/', '')

        # Ancestors enrichment
        ancestors_titles = []
        ancestors_links = []

        if 'ancestors' in page:
            ancestors = page['ancestors']
            if isinstance(ancestors, list):
                for ancestor in ancestors:
                    if 'title' in ancestor:
                        ancestors_titles.append(ancestor['title'])
                    else:
                        ancestors_titles.append(NO_ANCESTOR_TITLE)

                    ancestors_links.append(ancestor['_links']['webui'])

        eitem['ancestors_titles'] = ancestors_titles
        eitem['ancestors_links'] = ancestors_links

        # Specific enrichment
        if page['type'] == 'page':
            if page['version']['number'] == 1:
                eitem['type'] = 'new_page'
        eitem['is_blogpost'] = 0
        eitem['is_' + eitem['type']] = 1

        if self.sortinghat:
            eitem.update(self.get_item_sh(item))

        if self.prjs_map:
            eitem.update(self.get_item_project(eitem))

        eitem.update(self.get_grimoire_fields(eitem['date'], "confluence"))

        self.add_repository_labels(eitem)
        self.add_metadata_filter_raw(eitem)
        return eitem
