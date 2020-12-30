import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.type.type_command import TypeCommand
from model.type import Type


class FindTypes(TypeCommand):

    def __init__(self, project):
        self.project = project

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.project.id}/types")
            for tEntry in json.loads(json_obj):
                yield Type(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all time entries") from re
