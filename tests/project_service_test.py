import unittest

from business.project_service import ProjectService


class ProjectServiceTestCase(unittest.TestCase):
    proSer = ProjectService()

    def project_request(self):
        self.assertNotNull(self.proSer.request(1))
