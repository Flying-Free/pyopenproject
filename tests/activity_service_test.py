import unittest

from business.activity_service import ActivityService


class ActivityServiceTestCase(unittest.TestCase):
    actSer = ActivityService()


    def test_find_activity(self):
        self.assertNotNull(self.actSer.find(Activity()))

    def test_update_activity(self):
        self.assertNotNull(self.actSer.update(Activity()))
