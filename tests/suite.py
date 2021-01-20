import unittest

from tests.test_cases.activity_service_test import ActivityServiceTestCase
from tests.test_cases.attachment_service_test import AttachmentServiceTestCase
from tests.test_cases.budget_service_test import BudgetServiceTestCase
from tests.test_cases.category_service_test import CategoryServiceTestCase
from tests.test_cases.configuration_service_test import ConfigurationServiceTestCase
from tests.test_cases.custom_action_service_test import CustomActionServiceTestCase
from tests.test_cases.custom_object_service_test import CustomObjectServiceTestCase


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ActivityServiceTestCase))
    test_suite.addTest(unittest.makeSuite(AttachmentServiceTestCase))
    test_suite.addTest(unittest.makeSuite(BudgetServiceTestCase))
    test_suite.addTest(unittest.makeSuite(CategoryServiceTestCase))
    test_suite.addTest(unittest.makeSuite(ConfigurationServiceTestCase))
    test_suite.addTest(unittest.makeSuite(CustomActionServiceTestCase))
    test_suite.addTest(unittest.makeSuite(CustomObjectServiceTestCase))

    return test_suite


if __name__ == '__main__':
    mySuit = suite()

    runner = unittest.TextTestRunner()
    runner.run(mySuit)
