import unittest

from business.group_service import GroupService


class GridServiceTestCase(unittest.TestCase):
    groupSer = GroupService()

    def group_request(self):
        self.assertNotNull(self.groupSer.request(1))
