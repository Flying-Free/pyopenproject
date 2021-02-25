from pyopenproject import model as te
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PatchRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import TimeEntryCommand


class Update(TimeEntryCommand):

    def __init__(self, connection, time_entry):
        super().__init__(connection)
        self.time_entry = time_entry

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{self.time_entry.id}",
                                    json=self.time_entry.__dict__).execute()
            return te.TimeEntry(json_obj)

        except RequestError as re:
            raise BusinessError(f"Error deleting a time entry with ID: {self.time_entry.id}") from re
