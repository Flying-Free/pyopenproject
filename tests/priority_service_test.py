import json
import unittest

from business.priority_service import PriorityService


class PriorityServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.prioritySer = PriorityService()
        self.priority = json.loads('/data/priority.json')

    def test_find_all(self):
        self.assertNotNull(self.prioritySer.find(priority))

    def test_find_all(self):
        self.assertNotNull(self.prioritySer.find_all(filters))
