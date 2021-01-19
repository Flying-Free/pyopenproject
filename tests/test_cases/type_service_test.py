import json
import unittest

from business.services.type_service import TypeService
from model.type import Type


class TypeServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.typeSer = TypeService()
        with open('../data/type.json') as f:
            self.type = Type(json.load(f))

    def test_find_all(self):
        self.assertNotNull(self.typeSer.find_all())

    def test_find(self):
        self.assertNotNull(self.typeSer.find(self.type))
