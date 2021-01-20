import json

from business.exception.business_error import BusinessError
from model.category import Category
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class CategoryServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.catSer = self.factory.get_category_service()
        with open('../data/category.json') as f:
            self.category = Category(json.load(f))

    def test_find(self):
        # TODO: We need to create categories to test them
        pass

    def test_execute(self):
        # TODO: We need to create custom actions to test them
        pass

    def test_not_found(self):
        with self.assertRaises(BusinessError):
            self.catSer.find(self.category)

    def test_not_found_by_context(self):
        with self.assertRaises(BusinessError):
            self.catSer.find_by_context(f"/api/v3/categories/{self.category.id}")
