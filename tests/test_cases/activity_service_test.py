import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.model.activity import Activity
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class ActivityServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/activity.json')
        self.actSer = self.op.get_activity_service()
        with open(DATA) as f:
            self.activity = Activity(json.load(f))

    def test_activity_not_found(self):
        # There's no activity --> Exception
        with self.assertRaises(BusinessError):
            self.actSer.find(self.activity)

    def test_find_activity(self):
        activity = self.actSer.find(Activity({"id": "2"}))
        self.assertEqual(12, len(activity.details))

    def test_update_activity(self):
        activity = self.actSer.find(Activity({"id": "2"}))
        activity.comment['raw'] = "The updated comment"
        # FIXME: Bug "message":"Bad request: comment is invalid"
        # activity_updated = self.actSer.update(activity)
        # self.assertEqual(activity.comment, activity_updated.comment)
