import json
import unittest

from business.activity_service import ActivityService


class ActivityServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.actSer = ActivityService()
        self.activity = json.loads('/data/activity.json')

    def test_find_activity(self):
        self.assertNotNull(self.actSer.find(self.activity))

    def test_update_activity(self):
        self.assertNotNull(self.actSer.update(self.activity))
