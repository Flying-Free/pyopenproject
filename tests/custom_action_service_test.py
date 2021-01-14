import json
import unittest

from business.services.custom_action_service import CustomActionService


class CustomActionServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.caSer = CustomActionService()
        self.custom_action = json.loads('/data/custom_action.json')

    def execute(self):
        self.assertNotNull(self.caSer.execute(self.custom_action))

    def find(self):
        self.assertNotNull(self.caSer.find(self.custom_action))

