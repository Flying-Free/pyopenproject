import unittest

from business.status_service import StatusService


class StatusServiceTestCase(unittest.TestCase):
    statusSer = StatusService()

    def test_find(self):
        self.assertNotNull(self.statusSer.find(status))

    def test_find_all(self):
        self.assertNotNull(self.statusSer.find_all())

    def test_find_by_context(self, context):
        self.assertNotNull(self.statusSer.find_by_context(context))

