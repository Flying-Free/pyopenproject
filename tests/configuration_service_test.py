import json
import unittest

from business.service_factory import ServiceFactory
from model.configuration import Configuration


class ConfigurationServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.confSer = ServiceFactory.get_configuration_service()
        with open('./data/configuration.json') as f:
            self.configuration = Configuration(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.confSer.find())

    def test_same_config(self):
        current = self.confSer.find()
        expected = self.configuration
        self.assertEqual(expected.__dict__, current.__dict__)

