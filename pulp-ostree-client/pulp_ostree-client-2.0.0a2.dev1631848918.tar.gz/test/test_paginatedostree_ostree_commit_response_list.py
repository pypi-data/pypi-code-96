# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.models.paginatedostree_ostree_commit_response_list import PaginatedostreeOstreeCommitResponseList  # noqa: E501
from pulpcore.client.pulp_ostree.rest import ApiException

class TestPaginatedostreeOstreeCommitResponseList(unittest.TestCase):
    """PaginatedostreeOstreeCommitResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedostreeOstreeCommitResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_ostree.models.paginatedostree_ostree_commit_response_list.PaginatedostreeOstreeCommitResponseList()  # noqa: E501
        if include_optional :
            return PaginatedostreeOstreeCommitResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulp_ostree.models.ostree/ostree_commit_response.ostree.OstreeCommitResponse(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        artifact = '0', 
                        parent_commit = '0', 
                        checksum = '0', )
                    ]
            )
        else :
            return PaginatedostreeOstreeCommitResponseList(
        )

    def testPaginatedostreeOstreeCommitResponseList(self):
        """Test PaginatedostreeOstreeCommitResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
