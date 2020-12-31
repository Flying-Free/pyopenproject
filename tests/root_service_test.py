import unittest

from business.root_service import RootService


class RootServiceTestCase(unittest.TestCase):
    rootSer = RootService()

    def root_request(self):
        self.assertNotNull(self.rootSer.request(1))
