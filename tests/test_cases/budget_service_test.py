import json

from business.exception.business_error import BusinessError
from model.budget import Budget
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class BudgetServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.budSer = self.factory.get_budget_service()
        with open('../data/budget.json') as f:
            self.budget = Budget(json.load(f))

    def test_find(self):
        # TODO: We need a way to create a budget in order to change it
        # current = self.budSer.find(self.budget)
        # self.assertIsNotNone(current)
        pass

    def test_not_found(self):
        # There's no budget --> Exception
        with self.assertRaises(BusinessError):
            self.budSer.find(self.budget)
