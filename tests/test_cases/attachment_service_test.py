import json
import os
from pathlib import Path

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
        # TODO:  Error Traceback (most recent call last): File
        #  "($HOME)\Documents\GitHub\python-openproject-api\api_connection\request.py", line 21,
        #  in execute response.raise_for_status() File "C:\Python39\lib\site-packages\requests\models.py", line 943,
        #  in raise_for_status raise HTTPError(http_error_msg, response=self) requests.exceptions.HTTPError: 406
        #  Client Error: Not Acceptable for url: http://127.0.0.1:8080/api/v3/attachments/3
        #  The above exception was the direct cause of the following exception:
        #  Traceback (most recent call last): File
        #  "($HOME)\Documents\GitHub\python-openproject-api\business\services\impl\command\attachment
        #  \delete.py", line 15, in execute DeleteRequest(self.connection, f"{self.CONTEXT}/{
        #  self.attachment.id}").execute() File
        #  "($HOME)\Documents\GitHub\python-openproject-api\api_connection\request.py", line 42,
        #  in execute raise RequestError(f"Error running request with the URL: '{self.connection.url_base +
        #  self.context}'." + api_connection.exceptions.request_exception.RequestError: Error running request with the
        #  URL: 'http://127.0.0.1:8080/api/v3/attachments/3'. Missing content-type header
        #  The above exception was the direct cause of the following exception:
        #  Traceback (most recent call last): File "C:\Python39\lib\unittest\case.py", line 59, in testPartExecutor
        #  yield File "C:\Python39\lib\unittest\case.py", line 593, in run self._callTestMethod(testMethod) File
        #  "C:\Python39\lib\unittest\case.py", line 550, in _callTestMethod method() File
        #  "($HOME)\Documents\GitHub\python-openproject-api\tests\test_cases\attachment_service_test.py
        #  ", line 32, in test_delete self.assertIsNotNone(self.attSer.delete(self.created_attachment)) File
        #  "($HOME)\Documents\GitHub\python-openproject-api\business\services\impl
        #  \attachment_service_impl.py", line 17, in delete return Delete(self.connection, attachment).execute() File
        #  "($HOME)\Documents\GitHub\python-openproject-api\business\services\impl\command\attachment
        #  \delete.py", line 17, in execute raise BusinessError(f"Error deleting attachment: {
        #  self.attachment.fileName}") from re business.exception.business_error.BusinessError: Error deleting
        #  attachment: cute-cat.png
        created_attachment = self.attSer.create(filename="cute-cat.png",
                                                description="A cute kitty, cuddling with its friends!",
                                                file_path='../img/cute-cat.png')
        self.attSer.delete(created_attachment)
        self.assertIsNone(self.attSer.find(created_attachment))

    def test_find(self):
        a = Attachment({'id': 1})
        attachment = self.attSer.find(a)
        self.assertIsNotNone(attachment)
        self.assertEqual(self.attachment.__dict__, attachment.__dict__)

    def test_download_by_context(self):
        file_content = self.attSer.download_by_context(
            attachment=self.attachment,
            folder=f'{str(Path.home())}/Downloads')
        self.assertIsNotNone(file_content)
        self.assertTrue(Path(f'{str(Path.home())}/Downloads/{self.attachment.fileName}').is_file())
        os.remove(f'{str(Path.home())}/Downloads/{self.attachment.fileName}')
        self.assertFalse(Path(f'{str(Path.home())}/Downloads/{self.attachment.fileName}').is_file())
