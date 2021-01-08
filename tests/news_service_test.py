import unittest

from business.news_service import NewsService


class NewsServiceTestCase(unittest.TestCase):
    newsSer = NewsService()

    def test_find(self, news):
        self.assertNotNull(self.newsSer.find(news))

    def test_find_all(self, offset, pageSize, filters, sortBy):
        self.assertNotNull(self.newsSer.find_all(self, offset, pageSize, filters, sortBy))
