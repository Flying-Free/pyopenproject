import json

from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.time_entry.time_entry_command import TimeEntryCommand
from model.time_entry import TimeEntry


class Update(TimeEntryCommand):

    def __init__(self, time_entry):
        self.time_entry = time_entry

    def execute(self):
        try:
            json_obj = Connection().patch(f"{self.CONTEXT}/{self.time_entry.id}", json.dumps(self.time_entry.__dict__))
            return TimeEntry(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error deleting a time entry with ID: {self.time_entry.id}") from re
