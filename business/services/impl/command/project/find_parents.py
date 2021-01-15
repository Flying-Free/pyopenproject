import json

from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.project import Project


class FindParents(ProjectCommand):

    def __init__(self, filters, of, sortBy):
        self.filters = filters
        self.of = of
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = Connection().get(
                f"{self.CONTEXT}/available_parent_projects?{self.filters},{self.of},{self.sortBy}")
            for tEntry in json.loads(json_obj):
                yield Project(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding parents of project: {self.project.name}") from re
