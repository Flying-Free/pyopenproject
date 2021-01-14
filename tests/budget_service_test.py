import json
import unittest

from business.exception.business_error import BusinessError
from business.service_factory import ServiceFactory
from model.budget import Budget


class BudgetServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.budSer = ServiceFactory.get_budget_service()
        with open('./data/budget.json') as f:
            self.budget = Budget(json.load(f))

    def test_find(self):
        # TODO: We need a way to create a budget in order to change it
        # self.assertNotNull(self.budSer.find(self.budget))
        pass

    def test_not_found(self):
        # There's no budget --> Exception
        with self.assertRaises(BusinessError):
            self.budSer.find(self.budget)
