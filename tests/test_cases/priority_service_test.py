import json
import unittest

from business.services.priority_service import PriorityService
from model.priority import Priority


class PriorityServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.prioritySer = PriorityService()
        with open('../data/priority.json') as f:
            self.priority = Priority(json.load(f))

    def test_find_all(self):
        self.assertNotNull(self.prioritySer.find(self.priority))

    def test_find_all(self):
        self.assertNotNull(self.prioritySer.find_all(filters))
