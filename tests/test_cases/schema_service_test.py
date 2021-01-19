from business.services.schema_service import SchemaService


class SchemaServiceTestCase(OpenProjectTestCase):
    # OpenProject organization hasn't develop it yet
    def setUp(self):
        super().setUp()
        self.schemaSer = SchemaService()
