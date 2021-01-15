import json
import unittest

import yaml

from business.exception.business_error import BusinessError
from business.service_factory import ServiceFactory
from model.activity import Activity


class ActivityServiceTestCase(unittest.TestCase):

    def setUp(self):
        with open("../api_connection/config.yml", "r") as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        url_base = cfg["api_conn"]["host"] + ":" + str(cfg["api_conn"]["port"])
        api_user = cfg["api_conn"]["user"]
        api_key = cfg["api_conn"]["password"]

        self.factory = ServiceFactory(url=url_base, user=api_user, api_key=api_key)
        self.actSer = self.factory.get_activity_service()
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
