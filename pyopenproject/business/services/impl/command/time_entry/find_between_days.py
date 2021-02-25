from pyopenproject import model as te
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import TimeEntryCommand
from pyopenproject.business.util import URL
from pyopenproject.business.util import URLParameter


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
