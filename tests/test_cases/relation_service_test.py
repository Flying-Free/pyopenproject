import json
import unittest

from business.services.relation_service import RelationService
from model.relation import Relation


class RelationServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.relationSer = RelationService()
        with open('../data/relation.json') as f:
            self.relation = Relation(json.load(f))

    def test_find(self):
        self.assertNotNull(self.relationSer.find(self.relation))

    def test_update(self):
        self.assertNotNull(self.relationSer.update(self.relation))

    def test_delete(self):
        self.assertNotNull(self.relationSer.delete(self.relation))

    def test_find_schema(self):
        self.assertNotNull(self.relationSer.find_schema())

    def test_find_all(self):
        self.assertNotNull(self.relationSer.find_all(filters, sortBy))

    def test_update_form(self):
        self.assertNotNull(self.relationSer.update_form(self.relation))

    def find_by_context(self):
        self.assertNotNull(self.relationSer.find_by_context(context))
