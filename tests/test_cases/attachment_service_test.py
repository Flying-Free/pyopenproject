import json

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
        self.assertEqual(self.created_attachment.__dict__, created_attachment.__dict__)

    def test_delete(self):
        # TODO:  raise RequestError(f"Error running request with the URL:
        #  '{self.connection.url_base + self.context}'." +
        #  api_connection.exceptions.request_exception.RequestError:
        #  Error running request with the URL: 'http://127.0.0.1:8080/api/v3/attachments/3'.
        #  Missing content-type header
        #  The above exception was the direct cause of the following exception:
        self.assertIsNotNone(self.attSer.delete(self.created_attachment))

    def test_find(self):
        a = Attachment({'id': 1})
        attachment = self.attSer.find(a)
        self.assertIsNotNone(attachment)
        self.assertEqual(self.attachment.__dict__, attachment.__dict__)

    def test_download_by_context(self):
        file_content = self.attSer.download_by_context(self.attachment)
        print(file_content)
