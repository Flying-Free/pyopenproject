import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.user import User


class FindAvailableResponsibles(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,
                                  f"{self.CONTEXT}/{self.project.id}/work_packages/available_responsibles").execute()
            for tEntry in json.loads(json_obj):
                yield User(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding responsible of project: {self.project.name}") from re
