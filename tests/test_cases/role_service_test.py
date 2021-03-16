import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.util.filter import Filter
from pyopenproject.model.role import Role
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RoleServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/role.json')
        self.roleSer = self.op.get_role_service()
        with open(DATA) as f:
            self.role = Role(json.load(f))

    def test_find(self):
        roles = list(filter(lambda x: x.name == "Anonymous", self.roleSer.find_all()))
        self.assertEqual(1, len(roles))
        current = self.roleSer.find(roles[0])
        self.assertEqual(roles[0].__dict__, current.__dict__)

    def test_find_all(self):
        roles = self.roleSer.find_all([Filter("unit", "=", ["system"])])
        self.assertEqual(1, len(roles))
        roles = self.roleSer.find_all()
        self.assertEqual(6, len(roles))

    def test_not_found_by_context(self):
        with self.assertRaises(BusinessError):
            self.roleSer.find_by_context(f"/api/v3/roles/10000")
