from tests.test_cases.openproject_test_case import OpenProjectTestCase


class SchemaServiceTestCase(OpenProjectTestCase):
    # TODO: OpenProject organization hasn't develop it yet
    def setUp(self):
        super().setUp()
        self.schemaSer = self.factory.get_schema_service()
