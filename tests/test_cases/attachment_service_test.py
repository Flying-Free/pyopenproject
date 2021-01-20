import json
import os
from pathlib import Path

from business.exception.business_error import BusinessError
from model.attachment import Attachment
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class AttachmentServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.attSer = self.factory.get_attachment_service()
        with open('../data/attachment.json') as f:
            self.attachment = Attachment(json.load(f))
        with open('../data/attachment-created.json') as f:
            self.created_attachment = Attachment(json.load(f))

    def test_create(self):
        created_attachment = self.attSer.create(filename="cute-cat.png",
                                                description="A cute kitty, cuddling with its friends!",
                                                file_path='../img/cute-cat.png')
        self.assertIsNotNone(created_attachment)
        self.assertEqual(created_attachment.id, self.attSer.find(created_attachment).id)

    def test_delete(self):
        created_attachment = self.attSer.create(filename="cute-cat.png",
                                                description="A cute kitty, cuddling with its friends!",
                                                file_path='../img/cute-cat.png')
        created_attachment = self.attSer.find(created_attachment)
        self.attSer.delete(created_attachment)
        # Can't find a deleted attached: 404 Client Error: Not Found for url
        with self.assertRaises(BusinessError):
            self.attSer.find(created_attachment)

    def test_find(self):
        a = Attachment({'id': 1})
        attachment = self.attSer.find(a)
        self.assertIsNotNone(attachment)
        self.assertEqual(self.attachment.fileName, attachment.fileName)

    def test_download_by_context(self):
        file_content = self.attSer.download_by_context(
            attachment=self.attachment,
            folder=f'{str(Path.home())}/Downloads')
        self.assertIsNotNone(file_content)
        self.assertTrue(Path(f'{str(Path.home())}/Downloads/{self.attachment.fileName}').is_file())
        os.remove(f'{str(Path.home())}/Downloads/{self.attachment.fileName}')
        self.assertFalse(Path(f'{str(Path.home())}/Downloads/{self.attachment.fileName}').is_file())
