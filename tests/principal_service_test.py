import unittest

from business.principal_service import PrincipalService


class PrincipalServiceTestCase(unittest.TestCase):
    principalSer = PrincipalService()

    def test_find_all(self):
        self.assertNotNull(self.principalSer.find_all(filters))
