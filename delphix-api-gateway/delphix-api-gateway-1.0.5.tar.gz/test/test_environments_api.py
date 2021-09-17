"""
    Delphix API Gateway

    Delphix API Gateway API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@delphix.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import delphix.api.gateway
from delphix.api.gateway.api.environments_api import EnvironmentsApi  # noqa: E501


class TestEnvironmentsApi(unittest.TestCase):
    """EnvironmentsApi unit test stubs"""

    def setUp(self):
        self.api = EnvironmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_environment_by_id(self):
        """Test case for get_environment_by_id

        Returns an environment by ID.  # noqa: E501
        """
        pass

    def test_get_environments(self):
        """Test case for get_environments

        List all environments.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
