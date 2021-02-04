import json
import os

from model.query import Query
from tests.test_cases.openproject_test_case import OpenProjectTestCase
from util.Filter import Filter


class QueryServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/query.json')
        self.querySer = self.factory.get_query_service()
        with open(DATA) as f:
            self.query = Query(json.load(f))

    def test_update(self):
        self.assertIsNotNone(self.querySer.update(self.query))

    def test_find(self):
        self.assertIsNotNone(
            self.querySer.find(self.query))

    def test_delete(self):
        self.assertIsNotNone(self.querySer.delete(self.query))

    def test_star(self):
        self.assertIsNotNone(self.querySer.star(self.query))

    def test_unstar(self):
        self.assertIsNotNone(self.querySer.unstar(self.query))

    def test_find_all(self):
        queries = self.querySer.find_all([Filter("project_id", "!*", ["null"])])
        self.assertEqual(0, len(queries))

    def test_create(self):
        self.assertIsNotNone(self.querySer.create(self.query))

    def test_create_form(self):
        self.assertIsNotNone(self.querySer.create_form(form))

    def test_schema(self):
        self.assertIsNotNone(self.querySer.schema())
