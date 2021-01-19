import json

from business.services.root_service import RootService
from model.root import Root


class RootServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.rootSer = RootService()
        with open('../data/root.json') as f:
            self.root = Root(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.rootSer.find(self.root))
