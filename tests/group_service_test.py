import unittest

from business.group_service import GroupService


class GroupServiceTestCase(unittest.TestCase):
    groupSer = GroupService()

    def find(self):
        self.assertNotNull(self.groupSer.find(group))
