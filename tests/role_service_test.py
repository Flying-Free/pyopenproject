import unittest

from business.role_service import RoleService


class RoleServiceTestCase(unittest.TestCase):
    roleSer = RoleService()

    def render_request(self):
        self.assertNotNull(self.roleSer.request(1))
