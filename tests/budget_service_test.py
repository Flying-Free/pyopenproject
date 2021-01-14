import json
import unittest

from business.services.budget_service import BudgetService
from model.budget import Budget


class BudgetServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.budSer = BudgetService()
        with open('./data/budget.json') as f:
            self.budget = Budget(json.load(f))

    def test_find(self):
        self.assertNotNull(self.budSer.find(self.budget))
