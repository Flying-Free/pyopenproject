import unittest

from business.configuration_service import ConfigurationService


class ConfigurationServiceTestCase(unittest.TestCase):
    catSer = ConfigurationService()

    def test_find(self):
        self.assertNotNull(self.catSer.find())
