import json
import os

from model.form import Form
from model.query import Query
from tests.test_cases.openproject_test_case import OpenProjectTestCase
from util.Filter import Filter


class QueryServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/inputs/query.json')
        self.querySer = self.factory.get_query_service()
        with open(DATA) as f:
            self.query = Query(json.load(f))
        QUERY_FORM = os.path.join(self.TEST_CASES, '../data/inputs/query_form.json')
        with open(QUERY_FORM) as f:
            self.query_form = Form(json.load(f))

    def test_operations(self):
        # Create form
        qf=self.querySer.create_form(self.query_form)
        self.assertIsNotNone(qf)
        # Create
        query=self.querySer.create(self.query)
        self.assertIsNotNone(query)
        # Update TODO: FIXME: An internal error has occured. undefined method `to_sym' for nil:NilClass
        query.name = "Name after update"
        query_updated = self.querySer.update(query)
        self.assertIsNotNone(query)
        self.assertEqual(query_updated.name, query.name)
        # Find
        query = self.querySer.find(query_updated)
        self.assertIsNotNone(query)
        self.assertEqual(query.id, query_updated.id,)
        # Star
        self.assertIsNotNone(self.querySer.star(query))
        # Unstar
        self.assertIsNotNone(self.querySer.unstar(query))
        # Delete
        self.assertIsNotNone(self.querySer.delete(query))

    def test_find_all(self):
        queries = self.querySer.find_all()
        self.assertEqual(25, len(queries))
        queries = self.querySer.find_all([Filter("project_id", "!*", ["null"])])
        self.assertEqual(0, len(queries))

    def test_schema(self):
        self.assertIsNotNone(self.querySer.work_package())
