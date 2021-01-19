import json
import unittest

from business.services.post_service import PostService
from model.post import Post


class PostServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.postSer = PostService()
        with open('../data/post.json') as f:
            self.post = Post(json.load(f))

    def list_attachments(self):
        self.assertNotNull(self.postSer.list_attachments(self.post))

    def add_attachment(self):
        self.assertNotNull(self.postSer.add_attachment(self.post, attachment))

    def find(self):
        self.assertNotNull(self.postSer.find(self.post))
