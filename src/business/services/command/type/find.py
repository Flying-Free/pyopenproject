from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.get_request import GetRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.type.type_command import TypeCommand
from src.model.type import Type


class Find(TypeCommand):

    def __init__(self, connection, project_type):
        super().__init__(connection)
        self.project_type = project_type

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.project_type.id}").execute()
            return Type(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding type by ID: {self.project_type.id}") from re
