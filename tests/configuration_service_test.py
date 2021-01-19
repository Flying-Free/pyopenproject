import json
import unittest

import yaml

from business.service_factory import ServiceFactory
from model.configuration import Configuration


class ConfigurationServiceTestCase(unittest.TestCase):

    def setUp(self):
        with open("conf/config.yml", "r") as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        url_base = cfg["api_conn"]["host"] + ":" + str(cfg["api_conn"]["port"])
        api_user = cfg["api_conn"]["user"]
        api_key = cfg["api_conn"]["password"]

        self.factory = ServiceFactory(url=url_base, user=api_user, api_key=api_key)
        self.confSer = self.factory.get_configuration_service()
        with open('./data/configuration.json') as f:
            self.configuration = Configuration(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.confSer.find())

    def test_same_config(self):
        current = self.confSer.find()
        expected = self.configuration
        self.assertEqual(expected.__dict__, current.__dict__)
