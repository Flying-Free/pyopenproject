import unittest

from business.activity_service import ActivityService


class ActivityServiceTestCase(unittest.TestCase):
    actSer = ActivityService()

    def activity_request(self):
        self.assertNotNull(self.actSer.request(1))
