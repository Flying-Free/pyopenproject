from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.delete_request import DeleteRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.time_entry.time_entry_command import TimeEntryCommand


class Delete(TimeEntryCommand):

    def __init__(self, connection, time_entry):
        super().__init__(connection)
        self.time_entry = time_entry

    def execute(self):
        try:
            DeleteRequest(connection=self.connection,
                          context=f"{self.CONTEXT}/{self.time_entry.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error deleting a time entry with ID: {self.time_entry.id}") from re
