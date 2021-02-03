import json

from business.exception.business_error import BusinessError
from model.role import Role
from tests.test_cases.openproject_test_case import OpenProjectTestCase
from util.Filter import Filter


class RoleServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.roleSer = self.factory.get_role_service()
        with open('../data/role.json') as f:
            self.role = Role(json.load(f))

    # TODO: Not authorized
    def test_find(self):
        self.assertIsNotNone(self.roleSer.find(self.role))

    def test_find_all(self):
        roles = self.roleSer.find_all(Filter("unit", "=", "system"))
        self.assertEqual(1, len(roles))
        roles = self.roleSer.find_all()
        self.assertEqual(6, len(roles))

    # TODO: Not authorized
    def test_find_by_context(self):
        self.assertIsNotNone(self.roleSer.find_by_context('/api/v3/roles/3'))

    def test_not_found_by_context(self):
        with self.assertRaises(BusinessError):
            self.roleSer.find_by_context(f"/api/v3/roles/{self.role.id}")
