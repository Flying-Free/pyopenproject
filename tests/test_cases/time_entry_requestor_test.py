import datetime
import json

from dateutil.relativedelta import relativedelta

from model.time_entry import TimeEntry
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class TimeEntryServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.tEntryReq = self.factory.get_time_entry_service()
        with open('../data/time_entry.json') as f:
            self.time_entry = TimeEntry(json.load(f))

    def time_entries_request(self):
        today = datetime.today()
        end_date = today.strftime("%Y-%m-%d")
        start_date = datetime.today() + relativedelta(months=-3).strftime("%Y-%m-%d")
        self.tEntryReq.find_between_days(start_date, end_date)

    #TODO: Complete with methods