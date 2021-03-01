from tests.test_cases.openproject_test_case import OpenProjectTestCase


class SchemaServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.schemaSer = self.op.get_schema_service()

    # TODO: OpenProject organization hasn't develop it yet
