import unittest

from business.type_service import TypeService


class TypeServiceTestCase(unittest.TestCase):
    typeSer = TypeService()

    def type_request(self):
        self.assertNotNull(self.typeSer.request(1))
