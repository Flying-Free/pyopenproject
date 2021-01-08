import unittest

from business.document_service import DocumentService


class DocumentServiceTestCase(unittest.TestCase):
    docSer = DocumentService()

    def test_find(self):
        self.assertNotNull(self.docSer.find(document))

    def test_find_all(self):
        self.assertNotNull(self.docSer.find_all(offset, pageSize, sortBy))
