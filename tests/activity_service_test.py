import unittest

from business.activity_service import ActivityService


class ActivityServiceTestCase(unittest.TestCase):
    actSer = ActivityService()

    def find_activity(self):
        self.assertNotNull(self.actSer.find(Activity()))

    def update_activity(self):
        self.assertNotNull(self.actSer.update(Activity()))
