import unittest

from business.post_service import PostService


class PostServiceTestCase(unittest.TestCase):
    postSer = PostService()


    def list_attachments(self):
        self.assertNotNull(self.postSer.list_attachments(post))

    def add_attachment(self):
        self.assertNotNull(self.postSer.add_attachment(post, attachment))

    def find(self):
        self.assertNotNull(self.postSer.find(post))
