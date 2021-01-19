import json

from business.exception.business_error import BusinessError
from model.custom_action import CustomAction
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class CustomActionServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.caSer = self.factory.get_custom_action_service()
        with open('../data/custom_action.json') as f:
            self.custom_action = CustomAction(json.load(f))

    # TODO: We need to create custom actions to test them

    def test_not_found_executed(self):
        with self.assertRaises(BusinessError):
            self.assertIsNotNone(self.caSer.execute(self.custom_action))

    def test_find(self):
        with self.assertRaises(BusinessError):
            self.assertIsNotNone(self.caSer.find(self.custom_action))

