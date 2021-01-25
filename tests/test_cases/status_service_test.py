import json

from model.status import Status
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class StatusServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.statusSer = self.factory.get_status_service()
        with open('../data/status.json') as f:
            self.status = Status(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.statusSer.find(self.status))

    def test_find_all(self):
        statuses = self.statusSer.find_all()
        self.assertEqual(14, len(statuses))

    def test_find_by_context(self, context):
        self.assertIsNotNone(self.statusSer.find_by_context(context))
