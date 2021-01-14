import json
import unittest

from business.services.status_service import StatusService


class StatusServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.statusSer = StatusService()
        self.status = json.loads('/data/status.json')

    def test_find(self):
        self.assertNotNull(self.statusSer.find(self.status))

    def test_find_all(self):
        self.assertNotNull(self.statusSer.find_all())

    def test_find_by_context(self, context):
        self.assertNotNull(self.statusSer.find_by_context(context))

