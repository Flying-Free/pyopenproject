from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.schema import Schema


class FindSchema(ProjectCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/schemas").execute()
            return Schema(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding the version schema") from re
