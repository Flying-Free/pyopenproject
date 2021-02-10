import json
import os

from model.version import Version
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class VersionServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/version.json')
        self.versionSer = self.factory.get_version_service()
        with open(DATA) as f:
            self.version = Version(json.load(f))

    def test_find(self, ):
        self.assertIsNotNone(self.versionSer.find(self.version))

    def test_update(self):
        self.assertIsNotNone(self.versionSer.update(self.version))

    def test_delete(self):
        self.assertIsNotNone(self.versionSer.delete(self.version))

    def test_find_all(self):
        versions = self.versionSer.find_all()
        self.assertEqual(4, len(versions))
        #TODO: FIXME: Sharing filter not exist...
        #self.assertIsNotNone(self.versionSer.find_all([Filter("sharing", "*", ["system"])]))

    # TODO: FIXME:  {"_type":"Error","errorIdentifier":"urn:openproject-org:api:v3:errors:PropertyConstraintViolation","message":"Project can't be blank.","_embedded":{"details":{"attribute":"project"}}}
    def test_create(self):
        DATA = os.path.join(self.TEST_CASES, '../data/inputs/version.json')
        with open(DATA) as f:
            version = Version(json.load(f))
        self.assertIsNotNone(self.versionSer.create(version))

    def test_find_schema(self):
        self.assertIsNotNone(self.versionSer.find_schema())

    def test_create_form(self):
        self.assertIsNotNone(self.versionSer.create_form(self.version))

    def test_update_form(self):
        self.assertIsNotNone(self.versionSer.update_form(self.version))

    def test_find_projects(self):
        self.assertIsNotNone(self.versionSer.find_projects())
