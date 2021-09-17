"""
    Delphix API Gateway

    Delphix API Gateway API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@delphix.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import delphix.api.gateway
from delphix.api.gateway.api.engines_api import EnginesApi  # noqa: E501


class TestEnginesApi(unittest.TestCase):
    """EnginesApi unit test stubs"""

    def setUp(self):
        self.api = EnginesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_engine_by_id(self):
        """Test case for get_engine_by_id

        Returns an engine by ID.  # noqa: E501
        """
        pass

    def test_get_engines(self):
        """Test case for get_engines

        List all engines.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
