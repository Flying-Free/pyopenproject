from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.time_entry.time_entry_command import TimeEntryCommand


class Delete(TimeEntryCommand):

    def __init__(self, identifier):
        self.identifier = identifier

    def execute(self):
        try:
            Connection().delete(f"{self.CONTEXT}/{self.identifier}")
        except RequestError as re:
            raise BusinessError(f"Error deleting a time entry with ID: {self.identifier}") from re
