import json
import unittest

from business.services.news_service import NewsService


class NewsServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.newsSer = NewsService()
        self.new = json.loads('/data/new.json')

    def test_find(self):
        self.assertNotNull(self.newsSer.find(self.new))

    def test_find_all(self):
        self.assertNotNull(self.newsSer.find_all(self, offset, pageSize, filters, sortBy))
