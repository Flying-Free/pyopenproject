import unittest

from business.post_service import PostService


class PostServiceTestCase(unittest.TestCase):
    postSer = PostService()

    def post_request(self):
        self.assertNotNull(self.postSer.request(1))
