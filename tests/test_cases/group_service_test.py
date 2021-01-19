import json

from business.exception.business_error import BusinessError
from model.group import Group
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class GroupServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.groupSer = self.factory.get_group_service()
        with open('../data/group.json') as f:
            self.group = Group(json.load(f))

    def test_find(self):
        # There's no group to update --> Exception
        with self.assertRaises(BusinessError):
            self.groupSer.find(self.group)
