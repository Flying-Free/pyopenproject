import unittest

from business.principal_service import PrincipalService


class PrincipalServiceTestCase(unittest.TestCase):
    principalSer = PrincipalService()

    def principal_request(self):
        self.assertNotNull(self.principalSer.request(1))
