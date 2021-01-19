import unittest

from business.services.schema_service import SchemaService


class SchemaServiceTestCase(unittest.TestCase):
    # OpenProject organization hasn't develop it yet
    def setUp(self):
        self.schemaSer = SchemaService()