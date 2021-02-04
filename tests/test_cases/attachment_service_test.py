import json
import os
from pathlib import Path

from model.attachment import Attachment
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class AttachmentServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        ATTACHMENT = os.path.join(self.TEST_CASES, '../data/attachment.json')
        ATTACHMENT_TO_CREATE = os.path.join(self.TEST_CASES, '../data/attachment-created.json')
        self.IMAGE = os.path.join(self.TEST_CASES, '../img/cute-cat.png')
        self.attSer = self.factory.get_attachment_service()
        with open(ATTACHMENT) as f:
            self.attachment = Attachment(json.load(f))
        with open(ATTACHMENT_TO_CREATE) as f:
            self.created_attachment = Attachment(json.load(f))

    # FIXME
    #  {
    #  "_type":"Error",
    #  "errorIdentifier":"urn:openproject-org:api:v3:errors:InternalServerError",
    #  "message":"An internal error has occured. invalid %-encoding (\u0000\u0000��\u0000\u0000�\u0000\u0000\u0000��\u0000\u0000u0\u0000\u0000�`\u0000\u0000:�\u0000\u0000\u0017p��Q<\u0000\u0000\u0000\u0006bKGD\u0000�\u0000�\u0000�����\u0000\u0000\u0000\tpHYs\u0000\u0000\u000e�\u0000\u0000\u000e�\u0001�o�d\u0000\u0000�\u0000IDATxڬ�I�$I����Y6]m�%\"<\"2#�������\u0010n�\u0000\u0000�2�\n���\u0004�\u0001繀\b\u0018\u0002�\b�\u0001��\u0006�U�U�DFdl�ت����,��j��McI��n��*�\"������)"
    #  }
    # def test_create(self):
    #     created_attachment = self.attSer.create(filename="cute-cat.png",
    #                                             description="A cute kitty, cuddling with its friends!",
    #                                             file_path=self.IMAGE)
    #     self.assertIsNotNone(created_attachment)
    #     self.assertEqual(created_attachment.id, self.attSer.find(created_attachment).id)

    # def test_delete(self):
    #     created_attachment = self.attSer.create(filename="cute-cat.png",
    #                                             description="A cute kitty, cuddling with its friends!",
    #                                             file_path=self.IMAGE)
    #     created_attachment = self.attSer.find(created_attachment)
    #     self.attSer.delete(created_attachment)
    #     # Can't find a deleted attached: 404 Client Error: Not Found for url
    #     with self.assertRaises(BusinessError):
    #         self.attSer.find(created_attachment)

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
