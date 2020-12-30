from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.project.project_command import ProjectCommand
from model.schema import Schema


class FindSchema(ProjectCommand):

    def __init__(self, project):
        self.project = project

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/schemas")
            return Schema(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding the membership schema") from re