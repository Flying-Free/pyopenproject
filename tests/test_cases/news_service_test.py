import json

from model.new import New
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class NewsServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.newsSer = self.factory.get_news_service()
        with open('../data/new.json') as f:
            self.new = New(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.newsSer.find(self.new))

    def test_find_all(self):
        self.assertIsNotNone(self.newsSer.find_all(self, offset, pageSize, filters, sortBy))
