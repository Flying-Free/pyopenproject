import json
import unittest

from business.services.category_service import CategoryService
from model.category import Category


class CategoryServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.catSer = CategoryService()
        with open('./data/category.json') as f:
            self.category = Category(json.load(f))

    def test_find(self):
        self.assertNotNull(self.catSer.find(self.category))

    def test_find_by_context(self):
        self.assertNotNull(self.catSer.find_by_context(context))
