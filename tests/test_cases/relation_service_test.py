import json

from business.exception.business_error import BusinessError
from model.relation import Relation
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RelationServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.relationSer = self.factory.get_relation_service()
        with open('../data/relation.json') as f:
            self.relation = Relation(json.load(f))

    def test_find(self):
        # There's no relation --> Exception
        with self.assertRaises(BusinessError):
            self.assertIsNotNone(self.relationSer.find(self.relation))

    def test_update(self):
        self.assertIsNotNone(self.relationSer.update(self.relation))

    def test_delete(self):
        self.assertIsNotNone(self.relationSer.delete(self.relation))

    def test_find_schema(self):
        self.assertIsNotNone(self.relationSer.find_schema())

    def test_find_all(self):
        self.assertIsNotNone(self.relationSer.find_all(filters, sortBy))

    def test_update_form(self):
        self.assertIsNotNone(self.relationSer.update_form(self.relation))

    def find_by_context(self):
        self.assertIsNotNone(self.relationSer.find_by_context(context))
