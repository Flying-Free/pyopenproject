from pyopenproject import model as te
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import TimeEntryCommand


class FindByContext(TimeEntryCommand):

    def __init__(self, connection, context):
        super().__init__(connection)
        self.context = context

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.context}").execute()
            return te.TimeEntry(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding time entry by context: {self.context}") from re
