from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.time_entry.time_entry_command import TimeEntryCommand
import json

from src.extract.model.time_entry import TimeEntry


class FindBetweenDays(TimeEntryCommand):

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}?filters=[{{\"spentOn\":{{\"operator\":\"<>d\",\"values\":[\""
                                        f"{self.start_date},{self.end_date}\"]}}}}]")
            for tEntry in json_obj:
                yield TimeEntry(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding time entries between {self.start_date} and {self.end_date}") from re
