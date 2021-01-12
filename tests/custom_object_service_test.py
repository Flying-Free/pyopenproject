import json
import unittest

from business.custom_object_service import CustomObjectService


class CustomObjectServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.coSer = CustomObjectService()
        self.custom_object = json.loads('/data/custom_object.json')

    def test_find(self):
        self.assertNotNull(self.coSer.find(self.custom_object))
