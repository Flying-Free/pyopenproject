import unittest

from business.schema_service import SchemaService


class SchemaServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.schemaSer = SchemaService()