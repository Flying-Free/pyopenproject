from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.time_entry.time_entry_command import TimeEntryCommand
import model.time_entry as te
from util.Filters import Filters
from util.URL import URL
from util.URLParameter import URLParameter


class FindBetweenDays(TimeEntryCommand):

    def __init__(self, connection, start_date, end_date):
        super().__init__(connection)
        self.start_date = start_date
        self.end_date = end_date

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                          [
                                              URLParameter("startDate", self.start_date),
                                              URLParameter("endDate", self.end_date)
                                          ]))).execute()

            for tEntry in json_obj["_embedded"]["elements"]:
                yield te.TimeEntry(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding time entries between {self.start_date} and {self.end_date}") from re
