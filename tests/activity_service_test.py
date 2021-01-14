import json
import unittest

from business.service_factory import ServiceFactory
from model.activity import Activity


class ActivityServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.actSer = ServiceFactory.get_activity_service()
        self.activity = Activity(json.loads('./data/activity.json'))

    def test_find_activity(self):
        current = self.actSer.find(self.activity)
        self.assertNotNone(current)

    def test_update_activity(self):
        self.assertNotNull(self.actSer.update(self.activity))
