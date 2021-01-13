import json
import unittest

from business.relation_service import RelationService


class RelationServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.relationSer = RelationService()
        self.relation = json.loads('/data/relation.json')

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
