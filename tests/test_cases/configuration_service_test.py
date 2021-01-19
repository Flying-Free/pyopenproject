import json

from model.configuration import Configuration
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class ConfigurationServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.confSer = self.factory.get_configuration_service()
        with open('../data/configuration.json') as f:
            self.configuration = Configuration(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.confSer.find())

    def test_same_config(self):
        current = self.confSer.find()
        expected = self.configuration
        self.assertEqual(expected.__dict__, current.__dict__)
