import unittest

from business.budget_service import BudgetService


class BudgetServiceTestCase(unittest.TestCase):
    budSer = BudgetService()

    def budget_request(self):
        self.assertNotNull(self.budSer.request(1))
