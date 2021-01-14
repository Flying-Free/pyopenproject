from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.project import Project


class Delete(ProjectCommand):

    def __init__(self, project):
        self.project = project

    def execute(self):
        try:
            json_obj = Connection().delete(f"{self.CONTEXT}/{self.project.id}")
            return Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error deleting project: {self.project.name}") from re
