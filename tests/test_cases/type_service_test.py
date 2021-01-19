import json

from model.type import Type
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class TypeServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.typeSer = self.factory.get_type_service()
        with open('../data/type.json') as f:
            self.type = Type(json.load(f))

    def test_find_all(self):
        self.assertIsNotNone(self.typeSer.find_all())

    def test_find(self):
        self.assertIsNotNone(self.typeSer.find(self.type))
