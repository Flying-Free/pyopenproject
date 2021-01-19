import json
import unittest

from business.services.role_service import RoleService
from model.role import Role


class RoleServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.roleSer = RoleService()
        with open('../data/role.json') as f:
            self.role = Role(json.load(f))

    def test_find(self):
        self.assertNotNull(self.roleSer.find(self.role))

    def test_find_all(self):
        self.assertNotNull(self.roleSer.find_all())

    # TODO
    def test_find_by_context(self):
        self.assertNotNull(self.roleSer.find_by_context(context))
