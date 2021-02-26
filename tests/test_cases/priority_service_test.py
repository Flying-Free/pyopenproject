import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.model.priority import Priority
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class PriorityServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/priority.json')
        self.prioritySer = self.op.get_priority_service()
        with open(DATA) as f:
            self.priority = Priority(json.load(f))

    def test_not_found(self):
        # There's no priority --> Exception
        with self.assertRaises(BusinessError):
            self.prioritySer.find(self.priority)

    def test_find(self):
        expected = self.prioritySer.find_all()[-1]
        current = self.prioritySer.find(expected)
        self.assertEqual(expected.__dict__, current.__dict__)

    def test_find_all(self):
        priorities = self.prioritySer.find_all()
        self.assertEqual(4, len(priorities))
