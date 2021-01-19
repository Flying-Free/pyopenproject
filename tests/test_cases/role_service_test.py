import json

from model.role import Role
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RoleServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.roleSer = self.factory.get_role_service()
        with open('../data/role.json') as f:
            self.role = Role(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.roleSer.find(self.role))

    def test_find_all(self):
        self.assertIsNotNone(self.roleSer.find_all())

    # TODO
    def test_find_by_context(self):
        self.assertIsNotNone(self.roleSer.find_by_context(context))
