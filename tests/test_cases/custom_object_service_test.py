import json

from business.exception.business_error import BusinessError
from model.custom_object import CustomObject
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class CustomObjectServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.coSer = self.factory.get_custom_object_service()
        with open('../data/custom_object.json') as f:
            self.custom_object = CustomObject(json.load(f))

    def test_not_found(self):
        # Result is 404
        with self.assertRaises(BusinessError):
            self.coSer.find(self.custom_object)

    def test_find(self):
        # TODO: We need to create custom objects using the API
        pass
