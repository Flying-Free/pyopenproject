import json
import os

from business.exception.business_error import BusinessError
from model.project import Project
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

    def test_find(self):
        current = self.proSer.find(self.project)
        self.assertEqual(self.project.identifier, current.identifier)

    def test_update(self):
        # FIXME: Error Traceback (most recent call last): File
        #  "($HOME)\Documents\GitHub\python-openproject-api\api_connection\request.py", line 24, 
        #  in execute response.raise_for_status() File "C:\Python39\lib\site-packages\requests\models.py", line 943, 
        #  in raise_for_status raise HTTPError(http_error_msg, response=self) requests.exceptions.HTTPError: 500 
        #  Server Error: Internal Server Error for url: http://127.0.0.1:8080/api/v3/projects/2
        #  The above exception was the direct cause of the following exception:
        #  Traceback (most recent call last): File
        #  "($HOME)\Documents\GitHub\python-openproject-api\business\services\impl\command\project
        #  \update.py", line 18, in execute json_obj = PatchRequest(connection=self.connection,
        #  File "($HOME)\Documents\GitHub\python-openproject-api\api_connection\request.py", line 47,
        #  in execute raise RequestError(f"Error running request with the URL: "{self.connection.url_base +
        #  self.context}"." + api_connection.exceptions.request_exception.RequestError: Error running request with the
        #  URL: "http://127.0.0.1:8080/api/v3/projects/2". {"_type":"Error",
        #  "errorIdentifier":"urn:openproject-org:api:v3:errors:InternalServerError","message":"An internal error has
        #  occured. undefined method `fetch" for #<String:0x000055e39a848248>"}
        #  The above exception was the direct cause of the following exception:
        #  Traceback (most recent call last): File "C:\Python39\lib\unittest\case.py", line 59, in testPartExecutor
        #  yield File "C:\Python39\lib\unittest\case.py", line 593, in run self._callTestMethod(testMethod) File
        #  "C:\Python39\lib\unittest\case.py", line 550, in _callTestMethod method() File
        #  "($HOME)\Documents\GitHub\python-openproject-api\tests\test_cases\project_service_test.py",
        #  line 23, in test_update current = self.proSer.update(current) File
        #  "($HOME)\Documents\GitHub\python-openproject-api\business\services\impl\project_service_impl
        #  .py", line 30, in update return Update(self.connection, project).execute() File
        #  "($HOME)\Documents\GitHub\python-openproject-api\business\services\impl\command\project
        #  \update.py", line 23, in execute raise BusinessError(f"Error updating project: {self.project.name}") from
        #  re business.exception.business_error.BusinessError: Error updating project: Scrum project

        self.project = self.proSer.find(self.project)
        current = self.proSer.find(self.project)
        current.status = "new"
        current = self.proSer.update(current)
        self.assertEqual("new", current.status)
        current.status = self.project.status
        current = self.proSer.update(current)
        self.assertEqual(self.project.status, current.status)

    def test_delete(self):
        DATA = os.path.join(self.TEST_CASES, '../data/scrum_project.json')
        with open(DATA) as f:
            expected = Project(json.load(f))
        self.proSer.delete(self.project)
        expected = self.proSer.find(expected)
        self.assertEqual(False, expected.active)
        expected.active = True
        # TODO: review
        self.proSer.update(expected)
        self.assertEqual(True, expected.active)

    def test_find_all(self):
        projects = self.proSer.find_all()
        self.assertEqual(2, len(projects))

    def test_find_projects_with_filters(self):
        # TODO: Review filters CHANGE TO NEW HANDLE
        projects = self.proSer.find_all([Filter("active", "=", ["false"])])
        self.assertEqual(0, len(projects))

    def test_create(self):
        # TODO: Review creation
        p = Project({"name": "Test Project"})
        p = self.proSer.create(p)
        current = self.proSer.find(p)
        self.assertEqual("Test Project", current.name)

    def test_find_schema(self):
        # TODO
        self.assertIsNotNone(self.proSer.find_schema())

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
        # TODO
        self.assertIsNotNone(self.proSer.find_types(self.project))

    def test_find_budgets(self):
        budgets = self.proSer.find_budgets(self.project)
        self.assertEqual(0, len(budgets))

    def test_find_work_packages(self):
        #TODO: FIX ME: v3:errors:MissingPermission","message":"You are not authorized to access this resource."
        workpackages=self.proSer.find_work_packages(self.project, 1, 25, [Filter("status_id", "o", ["null"])],
            "status", '["status", "asc"]', "true")
        self.assertEqual(0, len(workpackages))

    def test_create_work_package(self):
        # TODO: FIX ME: An internal error has occured. can't convert String into Hash
        WORK_PACKAGE = os.path.join(self.TEST_CASES, '../data/work_package.json')
        with open(WORK_PACKAGE) as f:
            work_package = WorkPackage(json.load(f))
        self.assertIsNotNone(self.proSer.create_work_package(self.project, work_package))

    def test_create_work_package_form(self):
        # TODO: FIX ME: "You are not authorized to access this resource."
        WP_FORM = os.path.join(self.TEST_CASES, '../data/work_package_form.json')
        with open(WP_FORM) as f:
            work_package_form = WorkPackage(json.load(f))
        self.assertIsNotNone(self.proSer.create_work_package_form(self.project, work_package_form))

    def test_find_available_assignees(self):
        # TODO: FIX ME 404
        assignees=self.proSer.find_available_assignees(self.project)
        self.assertEqual(0, len(assignees))

    def test_find_available_responsibles(self):
        # TODO:
        self.assertIsNotNone(self.proSer.find_available_responsibles(self.project))
