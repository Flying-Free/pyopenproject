import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.time_entry.time_entry_command import TimeEntryCommand
from model.time_entry import TimeEntry


class Create(TimeEntryCommand):

    def __init__(self, connection, time_entry):
super().__init__(connection)        self.time_entry = time_entry

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}",
                                   json=json.dumps(self.time_entry.__dict__)).execute()
            return TimeEntry(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error deleting a time entry with ID: {self.time_entry.id}") from re
