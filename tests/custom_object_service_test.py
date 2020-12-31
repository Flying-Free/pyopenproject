import unittest

from business.custom_object_service import CustomObjectService


class CustomObjectServiceTestCase(unittest.TestCase):
    caSer = CustomObjectService()

    def custom_object_request(self):
        self.assertNotNull(self.caSer.request(1))
