import json
import os

from pyopenproject.business.util.filter import Filter
from pyopenproject.model.new import New
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class NewsServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/new.json')
        self.newsSer = self.op.get_news_service()
        with open(DATA) as f:
            self.new = New(json.load(f))

    def test_find(self):
        new = self.newsSer.find(self.new)
        self.assertEqual(new.title, self.new.title)

    def test_find_all(self):
        # Without filters
        news_list = self.newsSer.find_all(offset=None, page_size=None, filters=None, sort_by=None)
        self.assertEqual(2, len(news_list))
        # With filters
        news_list = self.newsSer.find_all(offset=1, page_size=2, filters=[Filter("project_id", "=", "1")],
                                          sort_by='[["created_at", "asc"]]')
        self.assertEqual(1, len(news_list))
        news_list = self.newsSer.find_all(offset=1, page_size=2, filters=[Filter("project_id", "=", "3")],
                                          sort_by='[["created_at", "asc"]]')
        self.assertEqual(0, len(news_list))
