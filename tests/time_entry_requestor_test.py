import datetime
import json
import unittest

from dateutil.relativedelta import relativedelta

from business.time_entry_service import TimeEntryService


class TimeEntryServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.tEntryReq = TimeEntryService()
        self.root = json.loads('/data/time_entry.json')

    def time_entries_request(self):
        today = datetime.today()
        end_date = today.strftime("%Y-%m-%d")
        start_date = datetime.today() + relativedelta(months=-3).strftime("%Y-%m-%d")
        self.tEntryReq.find_between_days(start_date, end_date)
