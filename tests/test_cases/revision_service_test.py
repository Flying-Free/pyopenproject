import json
import os

from model.revision import Revision
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RevisionServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/type.json')
        self.revisionSer = self.factory.get_revision_service()
        with open(DATA) as f:
            self.revision = Revision(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.revisionSer.find(self.revision))
