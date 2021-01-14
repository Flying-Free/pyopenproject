import json
import unittest

from business.category_service import CategoryService


class CategoryServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.catSer = CategoryService()
        self.category = json.loads('/data/category.json')

    def test_find(self):
        self.assertNotNull(self.catSer.find(self.category))

    def test_find_by_context(self):
        self.assertNotNull(self.catSer.find_by_context(context))
