import json

from business.services.status_service import StatusService
from model.status import Status


class StatusServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.statusSer = StatusService()
        with open('../data/status.json') as f:
            self.status = Status(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.statusSer.find(self.status))

    def test_find_all(self):
        self.assertIsNotNone(self.statusSer.find_all())

    def test_find_by_context(self, context):
        self.assertIsNotNone(self.statusSer.find_by_context(context))
