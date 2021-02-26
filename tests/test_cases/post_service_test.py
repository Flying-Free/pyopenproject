import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.model.attachment import Attachment
from pyopenproject.model.post import Post
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class PostServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/post.json')
        self.postSer = self.op.get_post_service()
        with open(DATA) as f:
            self.post = Post(json.load(f))

    def test_list_attachments(self):
        # 404 Client Error: Not Found for url: http://127.0.0.1:8080/api/v3/posts/1
        # There's not any post in the application
        with self.assertRaises(BusinessError):
            self.postSer.list_attachments(self.post)

    def test_add_attachment(self):
        ATTACHMENT = os.path.join(self.TEST_CASES, '../data/attachment.json')
        with open(ATTACHMENT) as f:
            attachment = Attachment(json.load(f))
        # 404 Client Error: Not Found for url: http://127.0.0.1:8080/api/v3/posts/1
        # There's not any post in the application
        with self.assertRaises(BusinessError):
            IMG = os.path.join(self.TEST_CASES, '../img/cute-cat.png')
            self.postSer.add_attachment(post=self.post, attachment=attachment, file_path=IMG)

    def test_find(self):
        # 404 Client Error: Not Found for url: http://127.0.0.1:8080/api/v3/posts/1
        # There's not any post in the application
        with self.assertRaises(BusinessError):
            self.postSer.find(self.post)

    def test_create(self):
        # TODO: To perform this test we need the API endpoint to be performed
        pass
