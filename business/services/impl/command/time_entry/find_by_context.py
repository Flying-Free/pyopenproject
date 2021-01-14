from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.time_entry.time_entry_command import TimeEntryCommand
from model.time_entry import TimeEntry


class FindByContext(TimeEntryCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.context}")
            return TimeEntry(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding time entry by context: {self.context}") from re
