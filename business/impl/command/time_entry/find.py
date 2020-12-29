from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.time_entry.time_entry_command import TimeEntryCommand
from model.time_entry import TimeEntry


class Find(TimeEntryCommand):

    def __init__(self, time_entry):
        self.time_entry = time_entry

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.time_entry.id}")
            return TimeEntry(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding time entry by ID: {self.time_entry.id}") from re
