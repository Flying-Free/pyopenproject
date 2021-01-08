import unittest

from business.custom_action_service import CustomActionService


class CustomActionServiceTestCase(unittest.TestCase):
    caSer = CustomActionService()

    def execute(self):
        self.assertNotNull(self.caSer.execute(custom_action))

    def find(self):
        self.assertNotNull(self.caSer.find(custom_action))

