from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.time_entry.time_entry_command import TimeEntryCommand
from pyopenproject.model import time_entry as te


class Find(TimeEntryCommand):

    def __init__(self, connection, time_entry):
        super().__init__(connection)
        self.time_entry = time_entry

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.time_entry.id}").execute()
            return te.TimeEntry(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding time entry by ID: {self.time_entry.id}") from re
