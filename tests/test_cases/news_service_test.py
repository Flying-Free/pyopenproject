import json
import unittest

from business.services.news_service import NewsService
from model.new import New


class NewsServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.newsSer = NewsService()
        with open('../data/new.json') as f:
            self.new = New(json.load(f))

    def test_find(self):
        self.assertNotNull(self.newsSer.find(self.new))

    def test_find_all(self):
        self.assertNotNull(self.newsSer.find_all(self, offset, pageSize, filters, sortBy))
