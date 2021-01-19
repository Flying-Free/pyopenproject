import json
import unittest

from business.services.root_service import RootService
from model.root import Root


class RootServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.rootSer = RootService()
        with open('../data/root.json') as f:
            self.root = Root(json.load(f))

    def test_find(self):
        self.assertNotNull(self.rootSer.find(self.root))
