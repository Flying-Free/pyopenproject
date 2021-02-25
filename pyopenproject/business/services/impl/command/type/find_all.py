from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import TypeCommand
from pyopenproject.model import Type


class FindAll(TypeCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            for typ in json_obj["_embedded"]["elements"]:
                yield Type(typ)
        except RequestError as re:
            raise BusinessError("Error finding all time entries") from re
