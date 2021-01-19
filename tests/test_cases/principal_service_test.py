import json
import unittest

from business.services.principal_service import PrincipalService
from model.principal import Principal


class PrincipalServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.principalSer = PrincipalService()
        with open('../data/principal.json') as f:
            self.principal = Principal(json.load(f))

    def test_find_all(self):
        self.assertNotNull(self.principalSer.find_all(filters))
