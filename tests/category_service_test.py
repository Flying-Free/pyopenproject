import unittest

from business.category_service import CategoryService


class CategoryServiceTestCase(unittest.TestCase):
    catSer = CategoryService()

    def test_find(self):
        self.assertNotNull(self.catSer.find(category))

    def test_find_by_context(self):
        self.assertNotNull(self.catSer.find_by_context(context))
