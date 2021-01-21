import json

from business.exception.business_error import BusinessError
from model.project import Project
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class ProjectServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.proSer = self.factory.get_project_service()
        with open("../data/project.json") as f:
            self.project = Project(json.load(f))

    def test_find(self):
        current = self.proSer.find(self.project)
        self.assertEqual(self.project.__dict__, current.__dict__)

    def test_update(self):
        # TODO:Error Traceback (most recent call last): File 
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
        current = self.proSer.find(self.project)
        with open("../data/scrum_project.json") as f:
            expected = Project(json.load(f))
        self.assertEqual(expected.__dict__, current.__dict__)
        self.proSer.delete(self.project)
        # current = self.proSer.find(self.project)
        with self.assertRaises(BusinessError):
            self.proSer.find(self.project)

    def test_find_all(self):
        projects = self.proSer.find_all()
        self.assertEqual(2, len(projects))

    def test_find_projects_with_filters(self):
        # TODO: Review filters
        projects = self.proSer.find_all(filters="[{ \"active\": { \"operator\": \"=\", \"values\": [\"false\"] }\" }]")
        self.assertEqual(0, len(projects))

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
