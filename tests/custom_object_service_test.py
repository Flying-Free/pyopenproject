import unittest

from business.custom_object_service import CustomObjectService


class CustomObjectServiceTestCase(unittest.TestCase):
    caSer = CustomObjectService()

    def test_find(self):
        self.assertNotNull(self.caSer.find(custom_object))
