import unittest

from business.relation_service import RelationService


class RelationServiceTestCase(unittest.TestCase):
    relationSer = RelationService()

    def test_find(self):
        self.assertNotNull(self.relationSer.find(relation))

    def test_update(self):
        self.assertNotNull(self.relationSer.update(relation))

    def test_delete(self):
        self.assertNotNull(self.relationSer.delete(relation))

    def test_find_schema(self):
        self.assertNotNull(self.relationSer.find_schema())

    def test_find_all(self):
        self.assertNotNull(self.relationSer.find_all(filters, sortBy))

    def test_update_form(self):
        self.assertNotNull(self.relationSer.update_form(relation))

    def find_by_context(self):
        self.assertNotNull(self.relationSer.find_by_context(context))
