import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.user import User


class FindAvailableResponsibles(ProjectCommand):

    def __init__(self, project):
        self.project = project

    def execute(self):
        try:
            json_obj = Connection().get(
                f"{self.CONTEXT}/{self.project.id}/work_packages/available_responsibles")
            for tEntry in json.loads(json_obj):
                yield User(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding responsible of project: {self.project.name}") from re
