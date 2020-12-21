import datetime
import unittest

from dateutil.relativedelta import relativedelta

from business.impl.time_entry_service_impl import TimeEntryServiceImpl


class TimeEntriesServiceTestCase(unittest.TestCase):
    tEntryReq = TimeEntryServiceImpl()

    def time_entries_request(self):
        today = datetime.today()
        end_date = today.strftime("%Y-%m-%d")
        start_date = datetime.today() + relativedelta(months=-3).strftime("%Y-%m-%d")
        self.tEntryReq.find_between_days(start_date, end_date)
