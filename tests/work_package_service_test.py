import unittest

from business.work_package_service import WorkPackageService


class WorkPackageServiceTestCase(unittest.TestCase):
    wpSer = WorkPackageService()

    def work_package_request(self):
        self.assertNotNull(self.wpSer.find_by_id(1))
