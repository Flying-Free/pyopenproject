import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.time_entry.time_entry_command import TimeEntryCommand
from model.project import Project


class FindProjects(TimeEntryCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/available_projects")
            for tEntry in json.loads(json_obj):
                yield Project(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all projects by context: {self.context}") from re
