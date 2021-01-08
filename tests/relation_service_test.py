import unittest

from business.relation_service import RelationService


class RelationServiceTestCase(unittest.TestCase):
    relationSer = RelationService()

    def relation_request(self):
        self.assertNotNull(self.relationSer.request(1))

#TODO: Hear