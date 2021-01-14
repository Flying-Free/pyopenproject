import json
import unittest

from business.service_factory import ServiceFactory
from model.group import Group


class GroupServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.groupSer = ServiceFactory.get_group_service()
        with open('./data/group.json') as f:
            self.group = Group(json.load(f))

    def find(self):
        self.assertNotNull(self.groupSer.find(self.group))