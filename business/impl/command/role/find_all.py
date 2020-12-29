import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.role.role_command import RoleCommand
from model.role import Role


class FindAll(RoleCommand):

    def __init__(self, filters):
        self.filters = filters

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}?{self.filters}")
            for tEntry in json.loads(json_obj):
                yield Role(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all roles with filters: {self.filters}") from re
