import unittest

from tests.test_cases.configuration_service_test import ConfigurationServiceTestCase


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ConfigurationServiceTestCase))
    return test_suite


mySuit = suite()

runner = unittest.TextTestRunner()
runner.run(mySuit)
