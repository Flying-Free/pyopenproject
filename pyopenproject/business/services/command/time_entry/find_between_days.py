from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.find_list_command import FindListCommand
from pyopenproject.business.services.command.time_entry.time_entry_command import TimeEntryCommand
from pyopenproject.business.util.filter import Filter
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.model.time_entry import TimeEntry


class FindBetweenDays(TimeEntryCommand):

    def __init__(self, connection, start_date, end_date):
        super().__init__(connection)
        self.start_date = start_date
        self.end_date = end_date

    def execute(self):
        try:
            request = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                          [
                                                              Filters([
                                                                  Filter("spentOn", "<>d",
                                                                         [self.start_date, self.end_date])])
                                                          ])))
            return FindListCommand(self.connection, request, TimeEntry).execute()

        except RequestError as re:
            raise BusinessError(f"Error finding time entries between {self.start_date} and {self.end_date}") from re
