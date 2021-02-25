from pyopenproject import model as te
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import TimeEntryCommand


class Create(TimeEntryCommand):

    def __init__(self, connection, time_entry):
        super().__init__(connection)
        self.time_entry = time_entry

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}",
                                   json=self.time_entry.__dict__).execute()
            return te.TimeEntry(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating a time entry with ID: {self.time_entry.id}") from re
