import json
import os
from pathlib import Path

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.model.attachment import Attachment
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class AttachmentServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        ATTACHMENT = os.path.join(self.TEST_CASES, '../data/attachment.json')
        ATTACHMENT_TO_CREATE = os.path.join(self.TEST_CASES, '../data/attachment-created.json')
        self.IMAGE = os.path.join(self.TEST_CASES, '../img/cute-cat.png')
        self.attSer = self.op.get_attachment_service()
        with open(ATTACHMENT) as f:
            self.attachment = Attachment(json.load(f))
        with open(ATTACHMENT_TO_CREATE) as f:
            self.created_attachment = Attachment(json.load(f))

    def test_create_and_delete(self):
        created_attachment = self.attSer.create(filename="cute-cat.png",
                                                description="A cute kitty, cuddling with its friends!",
                                                file_path=self.IMAGE)
        self.assertIsNotNone(created_attachment)
        self.assertEqual(created_attachment.id, self.attSer.find(created_attachment).id)
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
