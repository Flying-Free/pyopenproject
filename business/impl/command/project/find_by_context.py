from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.project.project_command import ProjectCommand
from model.project import Project


class FindByContext(ProjectCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.context}")
            return Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding project by context: {self.context}") from re
