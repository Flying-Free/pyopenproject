import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.model.category import Category
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class CategoryServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        CATEGORY = os.path.join(self.TEST_CASES, '../data/category.json')
        self.catSer = self.op.get_category_service()
        with open(CATEGORY) as f:
            self.category = Category(json.load(f))

    def test_not_found(self):
        with self.assertRaises(BusinessError):
            self.catSer.find(self.category)

    def test_not_found_by_context(self):
        with self.assertRaises(BusinessError):
            self.catSer.find_by_context(f"/api/v3/categories/{self.category.id}")
