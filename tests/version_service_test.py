import unittest

from business.version_service import VersionService


class VersionServiceTestCase(unittest.TestCase):
    versionSer = VersionService()

    def version_request(self):
        self.assertNotNull(self.versionSer.request(1))
