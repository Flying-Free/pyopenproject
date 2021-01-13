import json
import unittest

from business.post_service import PostService


class PostServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.postSer = PostService()
        self.post = json.loads('/data/post.json')

    def list_attachments(self):
        self.assertNotNull(self.postSer.list_attachments(self.post))

    def add_attachment(self):
        self.assertNotNull(self.postSer.add_attachment(self.post, attachment))

    def find(self):
        self.assertNotNull(self.postSer.find(self.post))
