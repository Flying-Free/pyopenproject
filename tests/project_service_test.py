import unittest

from business.project_service import ProjectService


class ProjectServiceTestCase(unittest.TestCase):
    proSer = ProjectService()


    def test_find(self):
        self.assertNotNull(self.proSer.find(project))

    def test_update(self):
        self.assertNotNull(self.proSer.update(project))

    def test_delete(self):
        self.assertNotNull(self.proSer.delete(project))

    def test_find_all(self):
        self.assertNotNull(self.proSer.find_all(filters,sortBy))


    def test_create(self):
        self.assertNotNull(self.proSer.create(project))

    def test_find_schema(self):
        self.assertNotNull(self.proSer.find_schema())

    def test_create_form(self, project):
        self.assertNotNull(self.proSer.create_form(project))


    def test_update_form(self):
        self.assertNotNull(self.proSer.update_form(project))


    def test_find_parents(self):
        self.assertNotNull(self.proSer.find_parents(filters, of, sortBy))

    def test_find_versions(self):
        self.assertNotNull(self.proSer.find_versions(project))

    def test_find_types(self):
        self.assertNotNull(self.proSer.find_types(project))

    def test_find_budgets(self):
        self.assertNotNull(self.proSer.find_budgets(project))

    def test_find_work_packages(self):
        self.assertNotNull(self.proSer.find_work_packages(project))

    def test_create_work_package(self):
        self.assertNotNull(self.proSer.create_work_package(project, notify, workPackage))

    def test_create_work_package_form(self):
        self.assertNotNull(self.proSer.create_work_package_form(project, notify, form))

    def test_find_available_assignees(self):
        self.assertNotNull(self.proSer.find_available_assignees(project))

    def test_find_available_responsibles(self):
        self.assertNotNull(self.proSer.find_available_responsibles(project))
