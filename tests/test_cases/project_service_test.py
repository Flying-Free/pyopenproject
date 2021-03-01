import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.util.filter import Filter
from pyopenproject.model.project import Project
from pyopenproject.model.user import User
from pyopenproject.model.work_package import WorkPackage
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class ProjectServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/project.json')
        self.proSer = self.op.get_project_service()
        with open(DATA) as f:
            self.project = Project(json.load(f))

        USER_INPUT = os.path.join(self.TEST_CASES, '../data/inputs/user.json')
        self.usrSer = self.op.get_user_service()
        with open(USER_INPUT) as f:
            self.new_user = User(json.load(f))

        PROJECT_INPUT = os.path.join(self.TEST_CASES, '../data/inputs/project.json')
        with open(PROJECT_INPUT) as f:
            self.new_project = Project(json.load(f))
        self.wpSer = self.op.get_work_package_service()

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
        self.proSer.delete(project)

    def test_find_schema(self):
        schema = self.proSer.find_schema()
        self.assertIsNotNone(schema)
        self.assertEqual(schema.id['name'], 'ID')

    def test_create_form(self):
        # TODO
        # self.assertIsNotNone(self.proSer.create_form(self.project))
        pass

    def test_update_form(self):
        # TODO
        # self.assertIsNotNone(self.proSer.update_form(self.project))
        pass

    def test_find_parents(self):
        # Not found
        with self.assertRaises(BusinessError):
            self.proSer.find_parents([Filter("ancestor", "=", ["1"])], 123, '[["id", "asc"]]')
        # Parameters with None
        parents = self.proSer.find_parents(filters=[Filter("ancestor", "=", ["1"])])
        self.assertEqual(0, len(parents))

    def test_find_versions(self):
        # TODO
        # self.assertIsNotNone(self.proSer.find_versions(self.project))
        pass

    def test_find_types(self):
        types = self.proSer.find_types(self.project)
        self.assertEqual(6, len(types))

    # FIXME: v3:errors:MissingPermission","message":"You are not authorized to access this resource."
    def test_find_budgets(self):
        # budgets = self.proSer.find_budgets(self.project)
        # self.assertEqual(0, len(budgets))
        pass

    def test_find_work_packages(self):
        work_packages = self.proSer.find_work_packages(self.project, 1, 25, [Filter("type_id", "=", ["1", "2"])],
                                                       "status", '[["status", "asc"]]', "true")
        self.assertEqual(6, len(work_packages))

    def test_create_work_package(self):
        WORK_PACKAGE = os.path.join(self.TEST_CASES, '../data/inputs/work_package.json')
        with open(WORK_PACKAGE) as f:
            work_package = WorkPackage(json.load(f))
        wp = self.proSer.create_work_package(self.project, work_package)
        self.assertIsNotNone(wp)
        self.assertEqual(wp.subject, 'Lorem')
        self.assertIsNone(self.wpSer.delete(wp))

    def test_create_work_package_form(self):
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
