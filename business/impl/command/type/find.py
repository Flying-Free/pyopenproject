from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.type.type_command import TypeCommand
from model.type import Type


class Find(TypeCommand):

    def __init__(self, type):
        self.type = type

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.type.id}")
            return Type(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding type by ID: {self.type.id}") from re
