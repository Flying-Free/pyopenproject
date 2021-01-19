import json

from model.attachment import Attachment
from model.post import Post
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class PostServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.postSer = self.factory.get_post_service()
        with open('../data/post.json') as f:
            self.post = Post(json.load(f))

    def list_attachments(self):
        self.assertIsNotNone(self.postSer.list_attachments(self.post))

    def add_attachment(self):
        with open('../data/attachment.json') as f:
            attachment = Attachment(json.load(f))
        self.assertIsNotNone(self.postSer.add_attachment(self.post, attachment))

    def find(self):
        self.assertIsNotNone(self.postSer.find(self.post))
