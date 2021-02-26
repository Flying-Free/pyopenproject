import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.util.filter import Filter
from pyopenproject.model.form import Form
from pyopenproject.model.query import Query
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class QueryServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/inputs/query.json')
        self.querySer = self.op.get_query_service()
        with open(DATA) as f:
            self.query = Query(json.load(f))
        QUERY_FORM = os.path.join(self.TEST_CASES, '../data/inputs/query_form.json')
        with open(QUERY_FORM) as f:
            self.query_form = Form(json.load(f))

    def test_operations(self):
        # Create form
        qf = self.querySer.create_form(self.query_form)
        self.assertIsNotNone(qf)
        # Create
        query = self.querySer.create(self.query)
        query = self.querySer.find(query)
        self.assertIsNotNone(query)
        # FIXME: Can't Update Query because all its properties are not writable
        # query.name = "Name after update"
        # query_updated = self.querySer.update(query)
        # self.assertIsNotNone(query)
        # self.assertEqual(query_updated.name, query.name)
        # # Find
        # query = self.querySer.find(query_updated)
        # self.assertIsNotNone(query)
        # self.assertEqual(query.id, query_updated.id, )
        # Star
        q = self.querySer.star(query)
        self.assertEqual(True, q.starred)
        # Unstar
        q = self.querySer.unstar(query)
        self.assertEqual(False, q.starred)
        # Delete
        self.querySer.delete(query)
        # Not Found Query --> Exception
        with self.assertRaises(BusinessError):
            self.querySer.find(query)

    def test_find_all(self):
        queries = self.querySer.find_all()
        self.assertEqual(25, len(queries))
        queries = self.querySer.find_all([Filter("project_id", "!*", ["null"])])
        self.assertEqual(0, len(queries))

    def test_schema(self):
        schema = self.querySer.schema()
        self.assertIsNotNone(schema)
        self.assertEqual(schema.connection['_type'], 'Schema')
