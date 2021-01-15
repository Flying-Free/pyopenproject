import json
import unittest

from business.service_factory import ServiceFactory
from model.custom_object import CustomObject


class CustomObjectServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.coSer = ServiceFactory.get_custom_object_service()
        with open('./data/custom_object.json') as f:
            self.custom_object = CustomObject(json.load(f))

    def test_find(self):
        current = self.coSer.find(self.custom_object)
        self.assertIsNotNone(current)
