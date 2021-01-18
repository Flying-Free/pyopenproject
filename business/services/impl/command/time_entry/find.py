from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.time_entry.time_entry_command import TimeEntryCommand
from model.time_entry import TimeEntry


class Find(TimeEntryCommand):

    def __init__(self, connection, time_entry):
        super(connection)
        self.time_entry = time_entry

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.time_entry.id}").execute()
            return TimeEntry(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding time entry by ID: {self.time_entry.id}") from re
