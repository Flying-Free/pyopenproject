import unittest

from business.version_service import VersionService


class VersionServiceTestCase(unittest.TestCase):
    versionSer = VersionService()


    def find(self, version):
        self.assertNotNull(self.versionSer.request(1))

    def update_version(self, version):
        self.assertNotNull(self.versionSer.request(1))

    def delete_version(self, version):
        self.assertNotNull(self.versionSer.request(1))

    def find_all(self, filters):
        self.assertNotNull(self.versionSer.request(1))

    def new_version(self, version):
        self.assertNotNull(self.versionSer.request(1))

    def find_by_context(self, context):
        self.assertNotNull(self.versionSer.request(1))

    def find_schema(self):
        self.assertNotNull(self.versionSer.request(1))

    def new_version_form(self, version):
        self.assertNotNull(self.versionSer.request(1))

    def update_version_form(self, version):
        self.assertNotNull(self.versionSer.request(1))

    def find_projects(self):
        self.assertNotNull(self.versionSer.request(1))
