from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.role.role_command import RoleCommand
from model.role import Role


class Find(RoleCommand):

    def __init__(self, role):
        self.role = role

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.role.id}")
            return Role(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding role by id: {self.role.id}") from re
