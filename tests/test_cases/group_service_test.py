import json

from model.group import Group
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class GroupServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.groupSer = self.factory.get_group_service()
        with open('../data/group.json') as f:
            self.group = Group(json.load(f))

    def find(self):
        self.assertIsNotNone(self.groupSer.find(self.group))
