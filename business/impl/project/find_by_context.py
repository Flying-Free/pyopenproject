from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.project.project_command import ProjectCommand
from src.extract.model.project import Project


class FindByContext(ProjectCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.context}")
            return Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding project by context: {self.context}") from re
