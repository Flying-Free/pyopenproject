import unittest

from business.work_package_service import WorkPackageService


class WorkPackageServiceTestCase(unittest.TestCase):
    taskSer = WorkPackageService()

    def work_package_request(self):
        self.assertNotNull(self.taskSer.find_by_id(1))
