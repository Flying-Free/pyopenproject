import json
import unittest

from business.relation_service import RelationService


class RelationServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.relationSer = RelationService()
        self.relation = json.loads('/data/relation.json')

    def test_find(self):
        self.assertNotNull(self.relationSer.find(self.relation))

    def test_find_by_context(self):
        self.assertNotNull(self.relationSer.find_by_context(context))

