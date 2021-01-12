import unittest

from business.role_service import RoleService


class RoleServiceTestCase(unittest.TestCase):
    roleSer = RoleService()

    def test_find(self):
        self.assertNotNull(self.roleSer.find(role))

    def test_find_all(self):
        self.assertNotNull(self.roleSer.find_all())

    def test_find_by_context(self, context):
        self.assertNotNull(self.roleSer.find_by_context(context))
