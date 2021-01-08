import unittest

from business.priority_service import PriorityService


class PriorityServiceTestCase(unittest.TestCase):
    prioritySer = PriorityService()

    def test_find_all(self):
        self.assertNotNull(self.prioritySer.find(priority))

    def test_find_all(self):
        self.assertNotNull(self.prioritySer.find_all(filters))
