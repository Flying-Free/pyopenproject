import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.model.version import Version
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class VersionServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/version_openproject.json')
        self.versionSer = self.op.get_version_service()
        with open(DATA) as f:
            self.version = Version(json.load(f))

    def tes_not_found(self):
        # Not Found Version --> Exception
        with self.assertRaises(BusinessError):
            self.versionSer.find(self.version)

    def test_find(self, ):
        versions = self.versionSer.find_all()
        self.assertEqual(4, len(versions))
        v = versions[0]
        found = self.versionSer.find(v)
        self.assertEqual(v.name, found.name)
        self.assertEqual(v.status, found.status)

    def test_find_all(self):
        versions = self.versionSer.find_all()
        self.assertEqual(4, len(versions))
        # FIXME: Sharing filter not exist...
        # self.assertIsNotNone(self.versionSer.find_all([Filter("sharing", "*", ["system"])]))

    def test_operations(self):
        version = Version(self.versionSer.create_form(self.version)._embedded["payload"])
        version.name = "v4.0 Alpha"
        version._links = {
            "definingProject": {"href": "/api/v3/projects/2"}
        }
        version = self.versionSer.create(version)
        versions = list(map(lambda x: x.id, self.versionSer.find_all()))
        self.assertIn(version.id, versions)
        version.name = "Demo Version"
        updated_version = self.versionSer.update(version)
        self.assertEqual(version.name, updated_version.name)
        self.versionSer.delete(updated_version)
        with self.assertRaises(BusinessError):
            self.versionSer.find(updated_version)

    def test_find_schema(self):
        schema = self.versionSer.find_schema()
        self.assertIsNotNone(schema)
        self.assertEqual(schema.id['name'], 'ID')

    def test_create_form(self):
        form = self.versionSer.create_form(self.version)
        self.assertEqual("v3.0 Alpha", form._embedded["payload"]["name"])
        self.assertEqual({'format': 'plain',
                          'raw': 'This version has a description',
                          'html': '<p>This version has a description</p>'
                          }, form._embedded["payload"]["description"])

    def test_update_form(self):
        form = self.versionSer.create_form(self.version)
        legacy_form = form
        form.name = ""
        form.endDate = "2018-01-10"
        form.startDate = "2018-01-01"
        form.status = "closed",
        form.sharing = "system"
        form = self.versionSer.update_form(form)
        self.assertEqual("", form._embedded["payload"]["name"])
        self.assertEqual("2018-01-10", form._embedded["payload"]["endDate"])
        self.assertEqual("2018-01-01", form._embedded["payload"]["startDate"])
        self.assertEqual('["closed"]', form._embedded["payload"]["status"])
        self.assertEqual("system", form._embedded["payload"]["sharing"])
        self.versionSer.update_form(legacy_form)

    def test_find_projects(self):
        projects = self.versionSer.find_projects()
        self.assertEqual(2, len(projects))
