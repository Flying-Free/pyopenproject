import json

from model.root import Root
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RootServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.rootSer = self.factory.get_root_service()
        with open('../data/root.json') as f:
            self.root = Root(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.rootSer.find(self.root))
