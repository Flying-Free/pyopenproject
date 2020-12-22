from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.time_entry.time_entry_command import TimeEntryCommand
from model.time_entry import TimeEntry


class FindById(TimeEntryCommand):

    def __init__(self, identifier):
        self.identifier = identifier

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.identifier}")
            return TimeEntry(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding time entry by ID: {self.identifier}") from re
