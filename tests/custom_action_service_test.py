import unittest

from business.custom_action_service import CustomActionService


class CustomActionServiceTestCase(unittest.TestCase):
    caSer = CustomActionService()

    def custom_action_request(self):
        self.assertNotNull(self.caSer.request(1))
