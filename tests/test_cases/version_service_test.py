import json

from model.version import Version
from tests.test_cases.openproject_test_case import OpenProjectTestCase
from util.Filter import Filter


class VersionServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.versionSer = self.factory.get_version_service()
        with open('../data/version.json') as f:
            self.version = Version(json.load(f))

    def test_find(self, ):
        self.assertIsNotNone(self.versionSer.find(self.version))

    def test_update(self):
        self.assertIsNotNone(self.versionSer.update(self.version))

    def test_delete(self):
        self.assertIsNotNone(self.versionSer.delete(1))

    def test_find_all(self):
        self.assertIsNotNone(self.versionSer.find_all([Filter("sharing", "*", "system")]))

    def test_create(self):
        self.assertIsNotNone(self.versionSer.create(self.version))

    # TODO
    def test_find_by_context(self):
        self.assertIsNotNone(self.versionSer.find_by_context(context))

    def test_find_schema(self):
        self.assertIsNotNone(self.versionSer.find_schema())

    def test_create_form(self):
        self.assertIsNotNone(self.versionSer.create_form(self.version))

    def test_update_form(self):
        self.assertIsNotNone(self.versionSer.update_form(self.version))

    def test_find_projects(self):
        self.assertIsNotNone(self.versionSer.find_projects())
