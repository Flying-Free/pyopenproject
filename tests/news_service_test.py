import unittest

from business.news_service import NewsService


class NewsServiceTestCase(unittest.TestCase):
    newsSer = NewsService()

    def news_request(self):
        self.assertNotNull(self.newsSer.request(1))
