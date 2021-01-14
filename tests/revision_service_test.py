import json
import unittest

from business.revision_service import RevisionService


class RevisionServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.revisionSer = RevisionService()
        self.revision = json.loads('/data/revision.json')

    def test_find(self):
        self.assertNotNull(self.revisionSer.find(self.revision))

    def test_find_by_context(self):
        self.assertNotNull(self.revisionSer.find_by_context(context))

