import unittest

from business.attachment_service import AttachmentService


class AttachmentServiceTestCase(unittest.TestCase):
    attSer = AttachmentService()

    def attachment_request(self):
        self.assertNotNull(self.attSer.request(1))
