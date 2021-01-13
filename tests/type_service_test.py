import json
import unittest

from business.type_service import TypeService


class TypeServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.typeSer = TypeService()
        self.root = json.loads('/data/type.json')

    def test_find_all(self):
        self.assertNotNull(self.typeSer.find_all())

    def test_find(self):
        self.assertNotNull(self.typeSer.find(type))
