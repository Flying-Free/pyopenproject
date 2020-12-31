import unittest

from business.schema_service import SchemaService


class SchemaServiceTestCase(unittest.TestCase):
    schemaSer = SchemaService()

    def schema_request(self):
        self.assertNotNull(self.schemaSer.request(1))
