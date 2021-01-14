import json
import unittest

from business.exception.business_error import BusinessError
from business.service_factory import ServiceFactory
from model.category import Category


class CategoryServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.catSer = ServiceFactory.get_category_service()
        with open('./data/category.json') as f:
            self.category = Category(json.load(f))

    # TODO: We need to create categories to test them

    def test_not_found(self):
        with self.assertRaises(BusinessError):
            self.catSer.find(self.category)

    def test_not_found_by_context(self):
        with self.assertRaises(BusinessError):
            self.catSer.find_by_context(f"/api/v3/categories/{self.category.id}")
