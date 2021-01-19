import json

from model.project import Project
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class ProjectServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.proSer = self.factory.get_project_service()
        with open('../data/project.json') as f:
            self.project = Project(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.proSer.find(self.project))

    def test_update(self):
        self.assertIsNotNone(self.proSer.update(self.project))

    def test_delete(self):
        self.assertIsNotNone(self.proSer.delete(self.project))

    def test_find_all(self):
        self.assertIsNotNone(self.proSer.find_all(None, None))

    def test_create(self):
        self.assertIsNotNone(self.proSer.create(self.project))

    def test_find_schema(self):
        self.assertIsNotNone(self.proSer.find_schema())

    def test_create_form(self):
        self.assertIsNotNone(self.proSer.create_form(self.project))

    def test_update_form(self):
        self.assertIsNotNone(self.proSer.update_form(self.project))

    def test_find_parents(self):
        self.assertIsNotNone(self.proSer.find_parents(filters, of, sortBy))

    def test_find_versions(self):
        self.assertIsNotNone(self.proSer.find_versions(self.project))

    def test_find_types(self):
        self.assertIsNotNone(self.proSer.find_types(self.project))

    def test_find_budgets(self):
        self.assertIsNotNone(self.proSer.find_budgets(self.project))

    def test_find_work_packages(self):
        self.assertIsNotNone(self.proSer.find_work_packages(self.project))

    def test_create_work_package(self):
        self.assertIsNotNone(self.proSer.create_work_package(self.project, notify, workPackage))

    def test_create_work_package_form(self):
        self.assertIsNotNone(self.proSer.create_work_package_form(self.project, notify, form))

    def test_find_available_assignees(self):
        self.assertIsNotNone(self.proSer.find_available_assignees(self.project))

    def test_find_available_responsibles(self):
        self.assertIsNotNone(self.proSer.find_available_responsibles(self.project))
