
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.type.type_command import TypeCommand
from model.type import Type


class FindAll(TypeCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            for typ in json_obj["_embedded"]["elements"]:
                yield Type(typ)
        except RequestError as re:
            raise BusinessError(f"Error finding all time entries") from re
