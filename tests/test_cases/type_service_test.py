import json
import os

from pyopenproject.model.type import Type
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class TypeServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/type.json')
        self.typeSer = self.op.get_type_service()
        with open(DATA) as f:
            self.type = Type(json.load(f))

    def test_find_all(self):
        types = self.typeSer.find_all()
        self.assertEqual(7, len(types))

    def test_find(self):
        t = self.typeSer.find(self.type)
        self.assertIsNotNone(t)
        self.assertEqual(t.name, 'Task')
