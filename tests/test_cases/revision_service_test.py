import json
import unittest

from business.services.revision_service import RevisionService
from model.revision import Revision


class RevisionServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.revisionSer = RevisionService()
        with open('../data/type.json') as f:
            self.revision = Revision(json.load(f))

    def test_find(self):
        self.assertNotNull(self.revisionSer.find(self.revision))

    # TODO
    def test_find_by_context(self):
        self.assertNotNull(self.revisionSer.find_by_context(context))

