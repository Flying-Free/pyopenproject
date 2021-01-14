import json
import unittest

from business.impl.configuration_service_impl import ConfigurationServiceImpl
from model.configuration import Configuration


class ConfigurationServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.confSer = ConfigurationServiceImpl()
        with open('./data/configuration.json') as f:
            self.configuration = Configuration(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.confSer.find())
