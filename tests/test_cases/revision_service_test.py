import json

from business.services.revision_service import RevisionService
from model.revision import Revision


class RevisionServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.revisionSer = RevisionService()
        with open('../data/type.json') as f:
            self.revision = Revision(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.revisionSer.find(self.revision))

    # TODO
    def test_find_by_context(self):
        self.assertIsNotNone(self.revisionSer.find_by_context(context))
