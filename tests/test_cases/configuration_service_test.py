import json
import os

from pyopenproject.model.configuration import Configuration
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class ConfigurationServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        CONFIGURATION = os.path.join(self.TEST_CASES, '../data/configuration.json')
        self.confSer = self.op.get_configuration_service()
        with open(CONFIGURATION) as f:
            self.configuration = Configuration(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.confSer.find())

    def test_same_config(self):
        current = self.confSer.find()
        expected = self.configuration
        self.assertEqual(expected.__dict__, current.__dict__)
