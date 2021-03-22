from contextlib import suppress

from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.patch_request import PatchRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.time_entry.time_entry_command import TimeEntryCommand
from pyopenproject.model import time_entry as te


class Update(TimeEntryCommand):

    def __init__(self, connection, time_entry):
        super().__init__(connection)
        self.time_entry = time_entry

    def execute(self):
        try:
            time_entry_id = self.time_entry.id
            self.__remove_readonly_attributes()
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{time_entry_id}",
                                    json=self.time_entry.__dict__).execute()
            return te.TimeEntry(json_obj)

        except RequestError as re:
            raise BusinessError(f"Error updating a time entry with ID: {time_entry_id}") from re

    def __remove_readonly_attributes(self):
        with suppress(KeyError): del self.time_entry.__dict__["_type"]
        with suppress(KeyError): del self.time_entry.__dict__["_links"]["self"]
        with suppress(KeyError): del self.time_entry.__dict__["_links"]["user"]
        with suppress(KeyError): del self.time_entry.__dict__["id"]
        with suppress(KeyError): del self.time_entry.__dict__["createdAt"]
        with suppress(KeyError): del self.time_entry.__dict__["updatedAt"]