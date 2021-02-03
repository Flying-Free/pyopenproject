import json
import os
from datetime import datetime

from dateutil.relativedelta import relativedelta

from model.form import Form
from model.time_entry import TimeEntry
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class TimeEntryServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        TIME_ENTRY = os.path.join(self.TEST_CASES, '../data/time_entry.json')
        TIME_ENTRY_INPUT = os.path.join(self.TEST_CASES, '../data/inputs/time_entry_form.json')
        self.tEntryReq = self.factory.get_time_entry_service()
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

    def test_find_by_context(self):
        pass

    def test_find_all(self):
        time_entries = self.tEntryReq.find_all()
        self.assertEqual(0, len(time_entries))

    def test_find_schema(self):
        schema = self.tEntryReq.find_schema()
        self.assertIsNotNone(schema)

    def test_operations(self):
        # Create
        time_entry = self.tEntryReq.create(self.time_entry)
        # Update
        time_entry.hours = "PT5H30M"
        time_entry = self.tEntryReq.update(self.time_entry)
        self.assertNotEqual(self.time_entry, time_entry)
        # Find
        time_entry_find=self.tEntryReq.find(time_entry)
        self.assertEqual(time_entry, time_entry_find)
        # Delete
        time_entry = self.tEntryReq.delete(time_entry)
        self.assertNotEqual(self.time_entry, time_entry)

    def test_operations_form(self):
        # Create with form
        time_entry = self.tEntryReq.create_form(self.time_entry_form)
        # Update with form
        time_entry.hours = "PT8H"
        time_entry = self.tEntryReq.update_form(time_entry)
        self.assertNotEqual(self.time_entry, time_entry)
