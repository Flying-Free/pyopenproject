import json
import unittest

from business.document_service import DocumentService


class DocumentServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.docSer = DocumentService()
        self.document = json.loads('/data/document.json')

    def test_find(self):
        self.assertNotNull(self.docSer.find(self.document))

    def test_find_all(self):
        self.assertNotNull(self.docSer.find_all(offset, pageSize, sortBy))
