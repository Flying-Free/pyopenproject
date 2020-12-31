import unittest

from business.configuration_service import ConfigurationService


class ConfigurationServiceTestCase(unittest.TestCase):
    catSer = ConfigurationService()

    def category_request(self):
        self.assertNotNull(self.catSer.request(1))
