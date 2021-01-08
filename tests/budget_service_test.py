import unittest

from business.budget_service import BudgetService


class BudgetServiceTestCase(unittest.TestCase):
    budSer = BudgetService()

    def test_find(self):
        self.assertNotNull(self.budSer.find(budget))
