import json

from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.time_entry.time_entry_command import TimeEntryCommand
from src.extract.model.time_entry import TimeEntry


class FindByContext(TimeEntryCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.context}")
            return TimeEntry(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding time entry by context: {self.context}") from re
