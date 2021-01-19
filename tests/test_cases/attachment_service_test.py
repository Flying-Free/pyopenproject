import json

from model.attachment import Attachment
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class AttachmentServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.attSer = self.factory.get_attachment_service()
        with open('../data/attachment.json') as f:
            self.attachment = Attachment(json.load(f))

    def test_create(self):
        self.assertIsNotNone(self.attSer.create(self.attachment))

    def test_delete(self):
        self.assertIsNotNone(self.attSer.delete(self.attachment))

    def test_find(self):
        self.assertIsNotNone(self.attSer.find(self.attachment))

    def test_find_all(self):
        self.assertIsNotNone(self.attSer.find_all())

    def test_download_by_context(self, context):
        self.assertIsNotNone(self.attSer.download_by_context(1))
