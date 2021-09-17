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

'''Bugzilla Ocean feeder'''

from .elastic import ElasticOcean
from ..elastic_mapping import Mapping as BaseMapping


class Mapping(BaseMapping):

    @staticmethod
    def get_elastic_mappings(es_major):
        """Get Elasticsearch mapping.

        :param es_major: major version of Elasticsearch, as string
        :returns:        dictionary with a key, 'items', with the mapping
        """

        mapping = '''
         {
            "dynamic":true,
                "properties": {
                    "data": {
                        "properties": {
                            "long_desc": {
                                "dynamic": false,
                                "properties": {}
                            },
                            "short_desc": {
                                "dynamic": false,
                                "properties": {
                                    "__text__": {
                                        "type": "text",
                                        "index": true
                                    }
                                }
                            },
                            "activity": {
                                "dynamic": false,
                                "properties": {}
                            }
                        }
                    }
                }
        }
        '''

        return {"items": mapping}


class BugzillaOcean(ElasticOcean):
    """Bugzilla Ocean feeder"""

    mapping = Mapping

    def _fix_item(self, item):
        # Could be used for filtering
        product = item['data']['product'][0]['__text__']
        item['product'] = product
