import unittest

from business.root_service import RootService


class RootServiceTestCase(unittest.TestCase):
    rootSer = RootService()

    def test_find(self):
        self.assertNotNull(self.rootSer.find(role))
