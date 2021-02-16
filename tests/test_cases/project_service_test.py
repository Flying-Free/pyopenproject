import json
import os

from business.exception.business_error import BusinessError
from model.project import Project
from model.user import User
from model.work_package import WorkPackage
from tests.test_cases.openproject_test_case import OpenProjectTestCase
from util.Filter import Filter


class ProjectServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/project.json')
        self.proSer = self.factory.get_project_service()
        with open(DATA) as f:
            self.project = Project(json.load(f))

        USER_INPUT = os.path.join(self.TEST_CASES, '../data/inputs/user.json')
        self.usrSer = self.factory.get_user_service()
        with open(USER_INPUT) as f:
            self.new_user = User(json.load(f))

        PROJECT_INPUT = os.path.join(self.TEST_CASES, '../data/inputs/project.json')
        with open(DATA) as f:
            self.new_project = Project(json.load(f))
        self.wpSer = self.factory.get_work_package_service()

    def test_find(self):
        current = self.proSer.find(self.project)
        self.assertEqual(self.project.identifier, current.identifier)

    def test_find_all(self):
        projects = self.proSer.find_all()
        self.assertEqual(2, len(projects))

    def test_find_all_with_filters(self):
        # TODO: Review filters How filter with active?
        projects = self.proSer.find_all([Filter("id", "=", ["1"])])
        self.assertEqual(1, len(projects))

    def test_operations(self):
        # Create
        project = self.proSer.create(self.new_project)
        # Find
        current = self.proSer.find(project)
        self.assertEqual("New project name", current.name)
        # Update
        current.name = "New project name changed"
        project = self.proSer.update(current)
        self.assertEqual("New project name changed", project.name)
        # Delete TODO: FIX ME Permision denied
        self.proSer.delete(project)

    def test_find_schema(self):
        schema = self.proSer.find_schema()
        self.assertIsNotNone(schema)
        self.assertEqual(schema.id['name'], 'ID')

    def test_create_form(self):
        # TODO
        self.assertIsNotNone(self.proSer.create_form(self.project))

    def test_update_form(self):
        # TODO
        self.assertIsNotNone(self.proSer.update_form(self.project))

    def test_find_parents(self):
        # Not found
        with self.assertRaises(BusinessError):
            self.proSer.find_parents([Filter("ancestor", "=", ["1"])], 123, '[["id", "asc"]]')
        # Parameters with None
        parents=self.proSer.find_parents(filters=[Filter("ancestor", "=", ["1"])])
        self.assertEqual(0, len(parents))

    def test_find_versions(self):
        # TODO
        self.assertIsNotNone(self.proSer.find_versions(self.project))

    def test_find_types(self):
        #TODO: FIX ME: v3:errors:MissingPermission","message":"You are not authorized to access this resource."
        types = self.proSer.find_types(self.project)
        self.assertEqual(6, len(types))

    def test_find_budgets(self):
        #TODO: FIX ME: v3:errors:MissingPermission","message":"You are not authorized to access this resource."
        budgets = self.proSer.find_budgets(self.project)
        self.assertEqual(0, len(budgets))

    def test_find_work_packages(self):
        # TODO: NOTE: status_id filter ([{ "status_id": { "operator": "o", "values": null }}]) dont works
        workpackages = self.proSer.find_work_packages(self.project, 1, 25, [Filter("type_id", "=", ["1", "2"])],
                                                      "status", '[["status", "asc"]]', "true")
        self.assertEqual(6, len(workpackages))

    def test_create_work_package(self):
        WORK_PACKAGE = os.path.join(self.TEST_CASES, '../data/inputs/work_package.json')
        with open(WORK_PACKAGE) as f:
            work_package = WorkPackage(json.load(f))
        wp=self.proSer.create_work_package(self.project, work_package)
        self.assertIsNotNone(wp)
        self.assertEqual(wp.subject, 'Lorem')
        self.assertIsNone(self.wpSer.delete(wp))

    def test_create_work_package_form(self):
        # TODO: FIX ME: "You are not authorized to access this resource."
        WP_FORM = os.path.join(self.TEST_CASES, '../data/work_package_form.json')
        with open(WP_FORM) as f:
            work_package_form = WorkPackage(json.load(f))
        self.assertIsNotNone(self.proSer.create_work_package_form(self.project, work_package_form))

    def test_find_available_assignees(self):
        assignees = self.proSer.find_available_assignees(self.project)
        self.assertEqual(1, len(assignees))

    def test_find_available_responsibles(self):
        responsibles = self.proSer.find_available_responsibles(self.project)
        self.assertEqual(1, len(responsibles))
