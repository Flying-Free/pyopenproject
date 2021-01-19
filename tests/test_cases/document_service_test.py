import json

from model.document import Document
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class DocumentServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.docSer = self.factory.get_document_service()
        with open('../data/document.json') as f:
            self.custom_object = Document(json.load(f))

    def test_find(self):
        self.assertNotNull(self.docSer.find(self.document))

    def test_find_all(self):
        self.assertNotNull(self.docSer.find_all(offset, pageSize, sortBy))
