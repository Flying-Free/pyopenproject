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
        self.assertIsNotNone(self.principalSer.find_all(filters))
