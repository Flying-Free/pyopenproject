import json
import unittest

from business.root_service import RootService


class RootServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.rootSer = RootService()
        self.root = json.loads('/data/root.json')

    def test_find(self):
        self.assertNotNull(self.rootSer.find(self.root))
