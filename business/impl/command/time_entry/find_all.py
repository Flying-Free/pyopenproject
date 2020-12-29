import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.time_entry.time_entry_command import TimeEntryCommand
from model.time_entry import TimeEntry


class FindAll(TimeEntryCommand):

    def __init__(self, offset, pageSize, filters, sortBy):
        self.offset = offset
        self.pageSize = pageSize
        self.filters = filters
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}?{self.offset},{self.pageSize},{self.filters},{self.sortBy}")
            for tEntry in json.loads(json_obj):
                yield TimeEntry(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all time entries") from re
