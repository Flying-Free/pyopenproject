import json
import os
from datetime import datetime

from dateutil.relativedelta import relativedelta

from pyopenproject.model.form import Form
from pyopenproject.model.time_entry import TimeEntry
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class TimeEntryServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        TIME_ENTRY = os.path.join(self.TEST_CASES, '../data/time_entry.json')
        TIME_ENTRY_INPUT = os.path.join(self.TEST_CASES, '../data/inputs/time_entry_form.json')
        self.tEntryReq = self.op.get_time_entry_service()
        with open(TIME_ENTRY) as f:
            self.time_entry = TimeEntry(json.load(f))
        with open(TIME_ENTRY_INPUT) as f:
            self.time_entry_form = Form(json.load(f))

    def test_find_between_days(self):
        today = datetime.today()
        end_date = today.strftime("%Y-%m-%d")
        start_date = datetime.today() + relativedelta(months=-3)
        start_date = start_date.strftime("%Y-%m-%d")
        time_entries = self.tEntryReq.find_between_days(start_date, end_date)
        self.assertEqual(0, len(time_entries))

    def test_find_projects(self):
        projects = self.tEntryReq.find_projects(self.time_entry)
        self.assertEqual(0, len(projects))

    def test_find_all(self):
        time_entries = self.tEntryReq.find_all()
        self.assertEqual(0, len(time_entries))

    def test_find_schema(self):
        schema = self.tEntryReq.find_schema()
        self.assertIsNotNone(schema)

    def test_operations(self):
        # project = self.factory.get_project_service().find_all()[-1]
        # work_package = list(filter(lambda x: x._links["type"]["title"] == "Task",
        #                            self.factory.get_project_service().find_work_packages(project=project)))[-1]
        # # TODO Find Activity by Name
        # # Create with form
        # form = self.tEntryReq.create_form(
        #     project=project,
        #     work_package=work_package,
        #     activity=1,  # Management
        #     comment="Test comment",
        #     spent_on=datetime.now(),
        #     hours=timedelta(hours=4, minutes=35, seconds=30))
        # Create
        # time_entry = self.tEntryReq.create(self.time_entry)
        # # Update
        # time_entry.hours = isodate.duration_isoformat(timedelta(hours=5, minutes=30))
        # time_entry = self.tEntryReq.update(self.time_entry)
        # self.assertNotEqual(self.time_entry, time_entry)
        # # Find
        # time_entry_find = self.tEntryReq.find(time_entry)
        # self.assertEqual(time_entry, time_entry_find)
        # # Delete
        # time_entry = self.tEntryReq.delete(time_entry)
        # self.assertNotEqual(self.time_entry, time_entry)
        pass

    # FIXME: Error running request with the URL (HTTPError): 'http://127.0.0.1:8080/api/v3/time_entries/form'.
    #  {
    #  "_type":"Error",
    #  "errorIdentifier":"urn:openproject-org:api:v3:errors:MissingPermission",
    #  "message":"You are not authorized to access this resource."
    #  }
    def test_operations_form(self):
        # project = self.factory.get_project_service().find_all()[-1]
        # work_package = list(filter(lambda x: x._links["type"]["title"] == "Task",
        #                            self.factory.get_project_service().find_work_packages(project=project)))[
        #     -1]
        # TODO Find Activity by Name
        # Create with form
        # form = self.tEntryReq.create_form(
        #     project=project,
        #     work_package=work_package,
        #     activity=1,  # Management
        #     comment="Test comment",
        #     spent_on=datetime.now(),
        #     hours=timedelta(hours=4, minutes=35, seconds=30))
        # # Update with form
        # form.hours = isodate.duration_isoformat(timedelta(hours=8))  # "PT8H"
        # form = self.tEntryReq.update_form(form)
        pass
