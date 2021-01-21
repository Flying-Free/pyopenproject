import json

from model.priority import Priority
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class PriorityServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.prioritySer = self.factory.get_priority_service()
        with open('../data/priority.json') as f:
            self.priority = Priority(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.prioritySer.find(self.priority))

    def test_find_all(self):
        self.assertIsNotNone(self.prioritySer.find_all(filters))
