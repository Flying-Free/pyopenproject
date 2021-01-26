import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.time_entry.time_entry_command import TimeEntryCommand
from model.time_entry import TimeEntry


class FindAll(TimeEntryCommand):

    def __init__(self, connection, offset, page_size, filters, sort_by):
        super().__init__(connection)
        self.offset = offset
        self.page_size = page_size
        self.filters = filters
        self.sort_by = sort_by

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,
                                  f"{self.CONTEXT}?offset={self.offset}&pageSize={self.page_size}&filters={self.filters}"
                                  f"&sortBy={self.sort_by}")\
                .execute()
            for time_entry in json_obj["_embedded"]["elements"]:
                yield TimeEntry(time_entry)
        except RequestError as re:
            raise BusinessError(f"Error finding all time entries") from re
