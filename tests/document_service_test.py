import unittest

from business.document_service import DocumentService


class DocumentServiceTestCase(unittest.TestCase):
    docSer = DocumentService()

    def document_request(self):
        self.assertNotNull(self.docSer.request(1))
