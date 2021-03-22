import json
import os

from pyopenproject.business.util.filter import Filter
from pyopenproject.model.principal import Principal
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class PrincipalServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/principal.json')
        self.principalSer = self.op.get_principal_service()
        with open(DATA) as f:
            self.principal = Principal(json.load(f))

    def test_find_all(self):
        principals = self.principalSer.find_all(filters=None)
        self.assertEqual(1, len(principals))

    def test_filters(self):
        # Filter member cant be tested with default user
        users = self.principalSer.find_all([Filter("type", "=", ["User"])])
        self.assertEqual("User", users[0]._type)
        # groups = self.principalSer.find_all([Filter("member", "=", ["Scrum project"])])
        # self.assertEqual("Group", groups[0]._type)
