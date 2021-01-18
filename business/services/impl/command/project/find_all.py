import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.project import Project


class FindAll(ProjectCommand):
    def __init__(self, connection, filters, sortBy):
        super().__init__(connection)
        self.filters = filters
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}?{self.filters},{self.sortBy}").execute()
            for tEntry in json.loads(json_obj):
                yield Project(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all projects by context: {self.filters},{self.sortBy}") from re
