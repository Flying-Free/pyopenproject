import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.version.version_command import VersionCommand
from model.project import Project


class FindProjects(VersionCommand):

    def execute(self):
        try:
            json_obj = Connection().get(
                f"{self.CONTEXT}/available_projects")
            for tEntry in json.loads(json_obj):
                yield Project(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding projects available for versions") from re
