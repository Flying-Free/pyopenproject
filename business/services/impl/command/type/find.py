from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.type.type_command import TypeCommand
from model.type import Type


class Find(TypeCommand):

    def __init__(self, connection, type):
super().__init__(connection)        self.type = type

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.type.id}")
            return Type(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding type by ID: {self.type.id}") from re
