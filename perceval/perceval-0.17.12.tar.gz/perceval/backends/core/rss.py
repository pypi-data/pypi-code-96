# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2020 Bitergia
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
#     Alvaro del Castillo <acs@bitergia.com>
#     Santiago Dueñas <sduenas@bitergia.com>
#     Stephan Barth <stephan.barth@gmail.com>
#     Valerio Cosentino <valcos@bitergia.com>
#     Jesus M. Gonzalez-Barahona <jgb@gsyc.es>
#     Harshal Mittal <harshalmittal4@gmail.com>
#

import logging

import feedparser

from grimoirelab_toolkit.datetime import str_to_datetime

from ...backend import (Backend,
                        BackendCommand,
                        BackendCommandArgumentParser)
from ...client import HttpClient

CATEGORY_ENTRY = "entry"

logger = logging.getLogger(__name__)


class RSS(Backend):
    """RSS backend for Perceval.

    This class retrieves the entries from a RSS feed.
    To initialize this class the URL must be provided.
    The `url` will be set as the origin of the data.

    :param url: RSS url
    :param tag: label used to mark the data
    :param archive: archive to store/retrieve items
    :param ssl_verify: enable/disable SSL verification
    """
    version = '0.7.0'

    CATEGORIES = [CATEGORY_ENTRY]

    def __init__(self, url, tag=None, archive=None, ssl_verify=True):
        origin = url

        super().__init__(origin, tag=tag, archive=archive, ssl_verify=ssl_verify)
        self.url = url
        self.client = None

    def fetch(self, category=CATEGORY_ENTRY):
        """Fetch the entries from the url.

        The method retrieves all entries from a RSS url

        :param category: the category of items to fetch

        :returns: a generator of entries
        """
        kwargs = {}
        items = super().fetch(category, **kwargs)

        return items

    def fetch_items(self, category, **kwargs):
        """Fetch the entries

        :param category: the category of items to fetch
        :param kwargs: backend arguments

        :returns: a generator of items
        """
        logger.info("Looking for rss entries at feed '%s'", self.url)

        nentries = 0  # number of entries

        raw_entries = self.client.get_entries()
        entries = self.parse_feed(raw_entries)['entries']
        for item in entries:
            yield item
            nentries += 1

        logger.info("Total number of entries: %i", nentries)

    @classmethod
    def parse_feed(self, raw_entries):
        return feedparser.parse(raw_entries)

    @classmethod
    def has_archiving(cls):
        """Returns whether it supports archiving entries on the fetch process.

        :returns: this backend supports entries archive
        """
        return True

    @classmethod
    def has_resuming(cls):
        """Returns whether it supports to resume the fetch process.

        :returns: this backend does not supports entries resuming
        """
        return False

    @staticmethod
    def metadata_id(item):
        """Extracts the identifier from an entry item."""
        return str(item['link'])

    @staticmethod
    def metadata_updated_on(item):
        """Extracts the update time from a RSS item.

        The timestamp is extracted from 'published' field.
        This date is a datetime string that needs to be converted to
        a UNIX timestamp float value.

        :param item: item generated by the backend

        :returns: a UNIX timestamp
        """
        ts = str_to_datetime(item['published'])

        return ts.timestamp()

    @staticmethod
    def metadata_category(item):
        """Extracts the category from a RSS item.

        This backend only generates one type of item which is
        'entry'.
        """
        return CATEGORY_ENTRY

    def _init_client(self, from_archive=False):
        """Init client"""

        return RSSClient(self.url, self.archive, from_archive, self.ssl_verify)


class RSSClient(HttpClient):
    """RSS API client.

    This class implements a simple client to retrieve entries from
    projects in a RSS node.

    :param url: URL of rss node: https://item.opnfv.org/ci
    :param archive: an archive to store/read fetched data
    :param from_archive: it tells whether to write/read the archive
    :param ssl_verify: enable/disable SSL verification

    :raises HTTPError: when an error occurs doing the request
    """

    def __init__(self, url, archive=None, from_archive=False, ssl_verify=True):
        super().__init__(url, archive=archive, from_archive=from_archive, ssl_verify=ssl_verify)

    def get_entries(self):
        """ Retrieve all entries from a RSS feed"""

        req = self.fetch(self.base_url)
        return req.text


class RSSCommand(BackendCommand):
    """Class to run RSS backend from the command line."""

    BACKEND = RSS

    @classmethod
    def setup_cmd_parser(cls):
        """Returns the RSS argument parser."""

        parser = BackendCommandArgumentParser(cls.BACKEND,
                                              archive=True,
                                              ssl_verify=True)

        # Required arguments
        parser.parser.add_argument('url',
                                   help="URL of the RSS feed")

        return parser
