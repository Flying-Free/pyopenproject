import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.type.type_command import TypeCommand
from model.type import Type


class FindAll(TypeCommand):

    def __init__(self, connection):
        self.connection = connection

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            for tEntry in json.loads(json_obj):
                yield Type(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all time entries") from re
