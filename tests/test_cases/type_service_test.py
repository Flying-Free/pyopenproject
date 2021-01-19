import json

from business.services.type_service import TypeService
from model.type import Type


class TypeServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.typeSer = TypeService()
        with open('../data/type.json') as f:
            self.type = Type(json.load(f))

    def test_find_all(self):
        self.assertIsNotNone(self.typeSer.find_all())

    def test_find(self):
        self.assertIsNotNone(self.typeSer.find(self.type))
