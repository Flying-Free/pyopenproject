import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.version import Version


class FindVersions(ProjectCommand):

    def __init__(self, connection, project):
        self.project = project

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.project.id}/versions").execute()
            for tEntry in json.loads(json_obj):
                yield Version(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all time entries") from re