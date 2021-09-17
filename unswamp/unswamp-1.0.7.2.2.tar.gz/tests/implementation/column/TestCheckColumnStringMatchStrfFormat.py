from unittest import TestCase
from datetime import datetime
from tests.TestHelpers import TestHelpers
from unswamp.objects.checks import CheckColumnStringMatchStrfFormat


class TestCheckColumnStringMatchStrfFormat(TestCase):
    def setUp(self):
        key = TestHelpers.random_string()
        column = "Year"
        value = "%Y"
        active = TestHelpers.random_bool()
        meta_data = {"Date": datetime.today()}
        self.check_pass = CheckColumnStringMatchStrfFormat(
            key, column, value, active, meta_data)

        column = "Grade"
        self.check_fail = CheckColumnStringMatchStrfFormat(
            key, column, value, active, meta_data)

    def test_run_pass(self):
        check = self.check_pass
        expectation = True
        TestHelpers.test_run(self, check, expectation)

    def test_run_fail(self):
        check = self.check_fail
        expectation = False
        TestHelpers.test_run(self, check, expectation)
