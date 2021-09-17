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
#     Santiago Dueñas <sduenas@bitergia.com>
#     Alvaro del Castillo San Felix <acs@bitergia.com>
#     Stephan Barth <stephan.barth@gmail.com>
#     Valerio Cosentino <valcos@bitergia.com>
#     Jesus M. Gonzalez-Barahona <jgb@gsyc.es>
#     Harshal Mittal <harshalmittal4@gmail.com>
#

import json
import logging

import requests

from grimoirelab_toolkit.datetime import datetime_to_utc, str_to_datetime
from grimoirelab_toolkit.uris import urijoin

from ...backend import (Backend,
                        BackendCommand,
                        BackendCommandArgumentParser)
from ...client import HttpClient
from ...errors import BaseError, BackendError
from ...utils import DEFAULT_DATETIME


logger = logging.getLogger(__name__)

CATEGORY_BUG = "bug"
MAX_BUGS = 500  # Maximum number of bugs per query
MAX_CONTENTS = 25  # Maximum number of bug contents (history, comments) per query


class BugzillaREST(Backend):
    """Bugzilla backend that uses its API REST.

    This class allows the fetch the bugs stored in Bugzilla
    server (version 5.0 or later). To initialize this class
    the URL of the server must be provided. The `url` will be
    set as the origin of the data.

    :param url: Bugzilla server URL
    :param user: Bugzilla user
    :param password: Bugzilla user password
    :param api_token: Bugzilla token
    :param max_bugs: maximum number of bugs requested on the same query
    :param tag: label used to mark the data
    :param archive: archive to store/retrieve items
    :param ssl_verify: enable/disable SSL verification
    """
    version = '0.10.0'

    CATEGORIES = [CATEGORY_BUG]
    EXTRA_SEARCH_FIELDS = {
        'product': ['product'],
        'component': ['component']
    }

    def __init__(self, url, user=None, password=None, api_token=None,
                 max_bugs=MAX_BUGS, tag=None, archive=None, ssl_verify=True):
        origin = url

        super().__init__(origin, tag=tag, archive=archive, ssl_verify=ssl_verify)
        self.url = url
        self.user = user
        self.password = password
        self.api_token = api_token
        self.max_bugs = max(1, max_bugs)
        self.client = None

    def fetch(self, category=CATEGORY_BUG, from_date=DEFAULT_DATETIME):
        """Fetch the bugs from the repository.

        The method retrieves, from a Bugzilla repository, the bugs
        updated since the given date.

        :param category: the category of items to fetch
        :param from_date: obtain bugs updated since this date

        :returns: a generator of bugs
        """
        if not from_date:
            from_date = DEFAULT_DATETIME

        kwargs = {'from_date': from_date}
        items = super().fetch(category, **kwargs)

        return items

    def fetch_items(self, category, **kwargs):
        """Fetch the bugs

        :param category: the category of items to fetch
        :param kwargs: backend arguments

        :returns: a generator of items
        """

        from_date = kwargs['from_date']

        logger.info("Looking for bugs: '%s' updated from '%s'",
                    self.url, str(from_date))

        nbugs = 0
        for bug in self.__fetch_and_parse_bugs(from_date):
            nbugs += 1
            yield bug

        logger.info("Fetch process completed: %s bugs fetched", nbugs)

    @classmethod
    def has_archiving(cls):
        """Returns whether it supports archiving items on the fetch process.

        :returns: this backend supports items archive
        """
        return True

    @classmethod
    def has_resuming(cls):
        """Returns whether it supports to resume the fetch process.

        :returns: this backend supports items resuming
        """
        return True

    @staticmethod
    def metadata_id(item):
        """Extracts the identifier from a Bugzilla item."""

        return str(item['id'])

    @staticmethod
    def metadata_updated_on(item):
        """Extracts the update time from a Bugzilla item.

        The timestamp used is extracted from 'last_change_time' field.
        This date is converted to UNIX timestamp format taking into
        account the timezone of the date.

        :param item: item generated by the backend

        :returns: a UNIX timestamp
        """
        ts = item['last_change_time']
        ts = str_to_datetime(ts)

        return ts.timestamp()

    @staticmethod
    def metadata_category(item):
        """Extracts the category from a Bugzilla item.

        This backend only generates one type of item which is
        'bug'.
        """
        return CATEGORY_BUG

    def _init_client(self, from_archive=False):
        """Init client"""

        return BugzillaRESTClient(self.url, user=self.user, password=self.password, api_token=self.api_token,
                                  archive=self.archive, from_archive=from_archive, ssl_verify=self.ssl_verify)

    def __fetch_and_parse_bugs(self, from_date):
        max_contents = min(MAX_CONTENTS, self.max_bugs)
        offset = 0

        while True:
            logger.debug("Fetching and parsing bugs from: %s, offset: %s, limit: %s ",
                         str(from_date), offset, self.max_bugs)
            raw_bugs = self.client.bugs(from_date=from_date, offset=offset,
                                        max_bugs=self.max_bugs)

            data = json.loads(raw_bugs)
            buglist = data['bugs']

            tbugs = len(buglist)

            if tbugs == 0:
                break

            for i in range(0, tbugs, max_contents):
                chunk = buglist[i:i + max_contents]
                bug_ids = [b['id'] for b in chunk]

                comments = self.__fetch_and_parse_comments(*bug_ids)
                histories = self.__fetch_and_parse_histories(*bug_ids)
                attachments = self.__fetch_and_parse_attachments(*bug_ids)

                for bug in chunk:
                    bug_id = str(bug['id'])
                    bug['comments'] = comments[bug_id]
                    bug['history'] = histories[bug_id]
                    bug['attachments'] = attachments[bug_id]
                    yield bug

            offset += self.max_bugs

    def __fetch_and_parse_comments(self, *bug_ids):
        logger.debug("Fetching and parsing comments")
        raw_comments = self.client.comments(*bug_ids)
        return self.__parse_comments(raw_comments)

    def __fetch_and_parse_histories(self, *bug_ids):
        logger.debug("Fetching and parsing histories")
        raw_histories = self.client.history(*bug_ids)
        return self.__parse_histories(raw_histories)

    def __fetch_and_parse_attachments(self, *bug_ids):
        logger.debug("Fetching and parsing attachments")
        raw_attachments = self.client.attachments(*bug_ids)
        return self.__parse_attachments(raw_attachments)

    @staticmethod
    def __parse_comments(raw_comments):
        contents = json.loads(raw_comments)['bugs']
        comments = {k: v['comments'] for k, v in contents.items()}
        return comments

    @staticmethod
    def __parse_histories(raw_histories):
        contents = json.loads(raw_histories)['bugs']
        history = {str(c['id']): c['history'] for c in contents}
        return history

    @staticmethod
    def __parse_attachments(raw_attachments):
        contents = json.loads(raw_attachments)['bugs']
        attachments = {k: v for k, v in contents.items()}
        return attachments


class BugzillaRESTError(BaseError):
    """Raised when an error occurs using the API"""

    message = "%(error)s (code: %(code)s)"


class BugzillaRESTClient(HttpClient):
    """Bugzilla REST API client.

    This class implements a simple client to retrieve distinct
    kind of data from a Bugzilla > 5.0 repository using its
    REST API.

    When `user` and `password` parameters are given it logs in
    the server. Further requests will use the token obtained
    during the sign in phase.

    :param base_url: URL of the Bugzilla server
    :param user: Bugzilla user
    :param password: user password
    :param api_token: api token for user; when this is provided
        `user` and `password` parameters will be ignored
    :param archive: an archive to store/read fetched data
    :param from_archive: it tells whether to write/read the archive
    :param ssl_verify: enable/disable SSL verification

    :raises BackendError: when an error occurs initializing the
        client
    """
    URL = "%(base)s/rest/%(resource)s"

    # API resources
    RBUG = 'bug'
    RATTACHMENT = 'attachment'
    RCOMMENT = 'comment'
    RHISTORY = 'history'
    RLOGIN = 'login'

    # Resource parameters
    PBUGZILLA_LOGIN = 'login'
    PBUGZILLA_PASSWORD = 'password'
    PBUGZILLA_TOKEN = 'token'
    PIDS = 'ids'
    PLAST_CHANGE_TIME = 'last_change_time'
    PLIMIT = 'limit'
    POFFSET = 'offset'
    PORDER = 'order'
    PINCLUDE_FIELDS = 'include_fields'
    PEXCLUDE_FIELDS = 'exclude_fields'

    # Predefined values
    VCHANGE_DATE_ORDER = 'changeddate'
    VINCLUDE_ALL = '_all'
    VEXCLUDE_ATTCH_DATA = 'data'

    def __init__(self, base_url, user=None, password=None, api_token=None,
                 archive=None, from_archive=False, ssl_verify=True):
        super().__init__(base_url, archive=archive, from_archive=from_archive, ssl_verify=ssl_verify)

        self.api_token = api_token if api_token else None

        if user is not None and password is not None:
            self.login(user, password)

    def login(self, user, password):
        """Authenticate a user in the server.

        :param user: Bugzilla user
        :param password: user password
        """
        params = {
            self.PBUGZILLA_LOGIN: user,
            self.PBUGZILLA_PASSWORD: password
        }

        try:
            r = self.call(self.RLOGIN, params)
        except requests.exceptions.HTTPError as e:
            cause = ("Bugzilla REST client could not authenticate user %s. "
                     "See exception: %s") % (user, str(e))
            raise BackendError(cause=cause)

        data = json.loads(r)
        self.api_token = data['token']

    def bugs(self, from_date=DEFAULT_DATETIME, offset=None, max_bugs=MAX_BUGS):
        """Get the information of a list of bugs.

        :param from_date: retrieve bugs that where updated from that date;
            dates are converted to UTC
        :param offset: starting position for the search; i.e to return 11th
            element, set this value to 10.
        :param max_bugs: maximum number of bugs to reteurn per query
        """
        date = datetime_to_utc(from_date)
        date = date.strftime("%Y-%m-%dT%H:%M:%SZ")

        params = {
            self.PLAST_CHANGE_TIME: date,
            self.PLIMIT: max_bugs,
            self.PORDER: self.VCHANGE_DATE_ORDER,
            self.PINCLUDE_FIELDS: self.VINCLUDE_ALL
        }

        if offset:
            params[self.POFFSET] = offset

        response = self.call(self.RBUG, params)

        return response

    def comments(self, *bug_ids):
        """Get the comments of the given bugs.

        :param bug_ids: list of bug identifiers
        """
        # Hack. The first value must be a valid bug id
        resource = urijoin(self.RBUG, bug_ids[0], self.RCOMMENT)

        params = {
            self.PIDS: bug_ids
        }

        response = self.call(resource, params)

        return response

    def history(self, *bug_ids):
        """Get the history of the given bugs.

        :param bug_ids: list of bug identifiers
        """
        resource = urijoin(self.RBUG, bug_ids[0], self.RHISTORY)

        params = {
            self.PIDS: bug_ids
        }

        response = self.call(resource, params)

        return response

    def attachments(self, *bug_ids):
        """Get the attachments of the given bugs.

        :param bug_id: list of bug identifiers
        """
        resource = urijoin(self.RBUG, bug_ids[0], self.RATTACHMENT)

        params = {
            self.PIDS: bug_ids,
            self.PEXCLUDE_FIELDS: self.VEXCLUDE_ATTCH_DATA
        }

        response = self.call(resource, params)

        return response

    def call(self, resource, params):
        """Retrive the given resource.

        :param resource: resource to retrieve
        :param params: dict with the HTTP parameters needed to retrieve
            the given resource

        :raises BugzillaRESTError: raised when an error is returned by
            the server
        """
        url = self.URL % {'base': self.base_url, 'resource': resource}

        if self.api_token:
            params[self.PBUGZILLA_TOKEN] = self.api_token

        logger.debug("Bugzilla REST client requests: %s params: %s",
                     resource, str(params))

        r = self.fetch(url, payload=params)

        # Check for possible Bugzilla API errors
        result = r.json()

        if result.get('error', False):
            raise BugzillaRESTError(error=result['message'],
                                    code=result['code'])

        return r.text

    @staticmethod
    def sanitize_for_archive(url, headers, payload):
        """Sanitize payload of a HTTP request by removing the login, password and token information
        before storing/retrieving archived items

        :param: url: HTTP url request
        :param: headers: HTTP headers request
        :param: payload: HTTP payload request

        :returns url, headers and the sanitized payload
        """
        if BugzillaRESTClient.PBUGZILLA_LOGIN in payload:
            payload.pop(BugzillaRESTClient.PBUGZILLA_LOGIN)

        if BugzillaRESTClient.PBUGZILLA_PASSWORD in payload:
            payload.pop(BugzillaRESTClient.PBUGZILLA_PASSWORD)

        if BugzillaRESTClient.PBUGZILLA_TOKEN in payload:
            payload.pop(BugzillaRESTClient.PBUGZILLA_TOKEN)

        return url, headers, payload


class BugzillaRESTCommand(BackendCommand):
    """Class to run BugzillaREST backend from the command line."""

    BACKEND = BugzillaREST

    @classmethod
    def setup_cmd_parser(cls):
        """Returns the BugzillaREST argument parser."""

        parser = BackendCommandArgumentParser(cls.BACKEND,
                                              from_date=True,
                                              basic_auth=True,
                                              token_auth=True,
                                              archive=True,
                                              ssl_verify=True)

        # BugzillaREST options
        group = parser.parser.add_argument_group('Bugzilla REST arguments')
        group.add_argument('--max-bugs', dest='max_bugs',
                           type=int, default=MAX_BUGS,
                           help="Maximum number of bugs requested on the same query")

        # Required arguments
        parser.parser.add_argument('url',
                                   help="URL of the Bugzilla server")

        return parser
