import json
import unittest

from business.services.custom_action_service import CustomActionService
from model.custom_action import CustomAction


class CustomActionServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.caSer = CustomActionService()
        with open('./data/custom_action.json') as f:
            self.custom_action = CustomAction(json.load(f))

    def execute(self):
        self.assertNotNull(self.caSer.execute(self.custom_action))

    def find(self):
        self.assertNotNull(self.caSer.find(self.custom_action))

