import unittest

from business.attachment_service import AttachmentService


class AttachmentServiceTestCase(unittest.TestCase):
    attSer = AttachmentService()

    def test_create(self):
        self.assertNotNull(self.attSer.create(attachment))

    def test_delete(self):
        self.assertNotNull(self.attSer.delete(attachment))

    def test_find(self):
        self.assertNotNull(self.attSer.find(attachment))

    def test_find_all(self):
        self.assertNotNull(self.attSer.find_all())

    def test_download_by_context(self, context):
        self.assertNotNull(self.attSer.download_by_context(1))
