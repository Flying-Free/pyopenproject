import json

from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.project import Project


class Update(ProjectCommand):

    def __init__(self, project):
        self.project = project

    def execute(self):
        try:
            json_obj = Connection().patch(f"{self.CONTEXT}/{self.project.id}", json.dumps(self.project.__dict__))
            return Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating project: {self.project.name}") from re
