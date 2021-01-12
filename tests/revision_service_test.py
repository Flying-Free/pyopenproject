import unittest

from business.revision_service import RevisionService


class RelationServiceTestCase(unittest.TestCase):
    revisionSer = RevisionService()

    def test_find(self):
        self.assertNotNull(self.revisionSer.find(revision))

    def test_find_by_context(self, context):
        self.assertNotNull(self.revisionSer.find_by_context(context))

