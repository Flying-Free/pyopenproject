import json
import unittest

from business.services.principal_service import PrincipalService


class PrincipalServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.principalSer = PrincipalService()
        self.priority = json.loads('/data/principal.json')

    def test_find_all(self):
        self.assertNotNull(self.principalSer.find_all(filters))
