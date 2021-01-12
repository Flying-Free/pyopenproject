import json
import unittest

from business.configuration_service import ConfigurationService


class ConfigurationServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.confSer = ConfigurationService()
        self.configuration = json.loads('/data/configuration.json')

    def test_find(self):
        self.assertNotNull(self.confSer.find())
