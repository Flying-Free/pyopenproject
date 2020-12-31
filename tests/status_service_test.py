import unittest

from business.status_service import StatusService


class StatusServiceTestCase(unittest.TestCase):
    statusSer = StatusService()

    def status_request(self):
        self.assertNotNull(self.statusSer.request(1))
