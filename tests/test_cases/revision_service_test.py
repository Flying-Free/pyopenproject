import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.model.revision import Revision
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RevisionServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/type.json')
        self.revisionSer = self.op.get_revision_service()
        with open(DATA) as f:
            self.revision = Revision(json.load(f))

    def test_find(self):
        for i in range(1, 100):
            r = Revision({"id": i})
            # There's nt revisions available
            with self.assertRaises(BusinessError):
                self.revisionSer.find(r)
