import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.model.custom_action import CustomAction
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class CustomActionServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/custom_action.json')
        self.caSer = self.op.get_custom_action_service()
        with open(DATA) as f:
            self.custom_action = CustomAction(json.load(f))

    def test_executed(self):
        # TODO: We need to create custom actions to test them
        pass

    def test_find(self):
        # TODO: We need to create custom actions to test them
        pass

    def test_not_found_executed(self):
        with self.assertRaises(BusinessError):
            self.assertIsNotNone(self.caSer.execute(self.custom_action))

    def test_not_found(self):
        with self.assertRaises(BusinessError):
            self.assertIsNotNone(self.caSer.find(self.custom_action))
