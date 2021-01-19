import json

from model.revision import Revision
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RevisionServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.revisionSer = self.factory.get_revision_service()
        with open('../data/type.json') as f:
            self.revision = Revision(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.revisionSer.find(self.revision))

    # TODO
    def test_find_by_context(self):
        self.assertIsNotNone(self.revisionSer.find_by_context(context))
