import unittest

from business.category_service import CategoryService


class CategoryServiceTestCase(unittest.TestCase):
    catSer = CategoryService()

    def category_request(self):
        self.assertNotNull(self.catSer.request(1))
