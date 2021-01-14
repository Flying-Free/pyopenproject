import json
import unittest

from business.services.attachment_service import AttachmentService


class AttachmentServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.attSer = AttachmentService()
        self.attachment = json.loads('/data/attachment.json')

    def test_create(self):
        self.assertNotNull(self.attSer.create(self.attachment))

    def test_delete(self):
        self.assertNotNull(self.attSer.delete(self.attachment))

    def test_find(self):
        self.assertNotNull(self.attSer.find(self.attachment))

    def test_find_all(self):
        self.assertNotNull(self.attSer.find_all())

    def test_download_by_context(self, context):
        self.assertNotNull(self.attSer.download_by_context(1))
