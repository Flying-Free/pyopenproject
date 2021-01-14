import json
import unittest

from business.role_service import RoleService


class RoleServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.roleSer = RoleService()
        self.revision = json.loads('/data/role.json')

    def test_find(self):
        self.assertNotNull(self.roleSer.find(self.role))

    def test_find_all(self):
        self.assertNotNull(self.roleSer.find_all())

    def test_find_by_context(self):
        self.assertNotNull(self.roleSer.find_by_context(context))
