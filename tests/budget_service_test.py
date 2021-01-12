import json
import unittest

from business.budget_service import BudgetService


class BudgetServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.budSer = BudgetService()
        self.budget = json.loads('/data/budget.json')

    def test_find(self):
        self.assertNotNull(self.budSer.find(self.budget))
