import json
import unittest

from business.services.group_service import GroupService


class GroupServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.groupSer = GroupService()
        self.group = json.loads('/data/group.json')

    def find(self):
        self.assertNotNull(self.groupSer.find(self.group))