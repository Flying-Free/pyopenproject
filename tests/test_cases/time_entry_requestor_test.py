import datetime
import json

from dateutil.relativedelta import relativedelta

from business.services.time_entry_service import TimeEntryService
from model.time_entry import TimeEntry


class TimeEntryServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.tEntryReq = TimeEntryService()
        with open('../data/time_entry.json') as f:
            self.time_entry = TimeEntry(json.load(f))

    def time_entries_request(self):
        today = datetime.today()
        end_date = today.strftime("%Y-%m-%d")
        start_date = datetime.today() + relativedelta(months=-3).strftime("%Y-%m-%d")
        self.tEntryReq.find_between_days(start_date, end_date)

    #TODO: Complete with methods