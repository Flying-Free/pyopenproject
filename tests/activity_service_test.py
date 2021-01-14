import json
import unittest

from business.service_factory import ServiceFactory
from model.activity import Activity
from business.exception.business_error import BusinessError


class ActivityServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.actSer = ServiceFactory.get_activity_service()
        with open('./data/activity.json') as f:
            self.activity = Activity(json.load(f))

    def test_activity_not_found(self):
        # There's no activity --> Exception
        with self.assertRaises(BusinessError):
            self.actSer.find(self.activity)

    # TODO: Test to find an Activity

    def test_update_activity(self):
        # TODO: We need a way to create activity in order to change it
        # self.assertIsNotNone(self.actSer.update(self.activity))
        pass
