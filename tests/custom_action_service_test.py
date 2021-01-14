import json
import unittest

from business.exception.business_error import BusinessError
from business.service_factory import ServiceFactory
from model.custom_action import CustomAction


class CustomActionServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.caSer = ServiceFactory.get_custom_action_service()
        with open('./data/custom_action.json') as f:
            self.custom_action = CustomAction(json.load(f))

    def test_not_found_executed(self):
        with self.assertRaises(BusinessError):
            self.assertIsNotNone(self.caSer.execute(self.custom_action))

    def test_find(self):
        with self.assertRaises(BusinessError):
            self.assertIsNotNone(self.caSer.find(self.custom_action))

