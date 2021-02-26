import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.model.document import Document
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class DocumentServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/document.json')
        self.docSer = self.op.get_document_service()
        with open(DATA) as f:
            self.document = Document(json.load(f))

    def test_find(self):
        # TODO: We need a way to create a document using the API
        # current = self.docSer.find(self.document)
        # self.assertIsNotNone(current)
        pass

    def test_not_found(self):
        # Result is 404
        with self.assertRaises(BusinessError):
            self.docSer.find(self.document)

    def test_find_all(self):
        documents = self.docSer.find_all(25, 25, '[["created_at", "asc"]]')
        self.assertEqual(0, len(documents))
