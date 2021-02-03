import json
import os

from model.root import Root
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RootServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/root.json')
        self.rootSer = self.factory.get_root_service()
        with open(DATA) as f:
            self.root = Root(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.rootSer.find(self.root))
