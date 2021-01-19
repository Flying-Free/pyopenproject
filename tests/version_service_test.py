import json
import unittest

from business.services.version_service import VersionService
from model.version import Version


class VersionServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.versionSer = VersionService()
        with open('./data/version.json') as f:
            self.version = Version(json.load(f))

    def test_find(self, ):
        self.assertNotNull(self.versionSer.find(self.version))

    def test_update(self):
        self.assertNotNull(self.versionSer.update(self.version))

    def test_delete(self):
        self.assertNotNull(self.versionSer.delete(1))

    def test_find_all(self):
        self.assertNotNull(self.versionSer.find_all('[{ "sharing": { "operator": "*", "values": ["system"] }" }]'))

    def test_create(self):
        self.assertNotNull(self.versionSer.create(self.version))

    # TODO
    def find_by_context(self):
        self.assertNotNull(self.versionSer.find_by_context(context))

    def find_schema(self):
        self.assertNotNull(self.versionSer.find_schema())

    def create_form(self):
        self.assertNotNull(self.versionSer.create_form(self.version))

    def update_form(self):
        self.assertNotNull(self.versionSer.update_form(self.version))

    def find_projects(self):
        self.assertNotNull(self.versionSer.find_projects())
