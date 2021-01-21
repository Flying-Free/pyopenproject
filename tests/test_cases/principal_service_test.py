import json

from model.principal import Principal
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class PrincipalServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.principalSer = self.factory.get_principal_service()
        with open('../data/principal.json') as f:
            self.principal = Principal(json.load(f))

    def test_find_all(self):
        principals = self.principalSer.find_all(filters=None)
        self.assertEqual(1, len(principals))

    def test_filters(self):
        # TODO: review filters
        users = self.principalSer.find_all(filters='[{ "_type": { "operator": "=", "values": ["User"] }" }]')
        self.assertEqual(1, len(users))
        self.assertEqual("User", users[0]._type)
        groups = self.principalSer.find_all(filters='[{ "_type": { "operator": "=", "values": ["Group"] }" }]')
        self.assertEqual(1, len(groups))
        self.assertEqual("Group", groups[0]._type)
