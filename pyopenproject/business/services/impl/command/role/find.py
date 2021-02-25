from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import RoleCommand
from pyopenproject.model import Role


class Find(RoleCommand):

    def __init__(self, connection, role):
        super().__init__(connection)
        self.role = role

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.role.id}").execute()
            return Role(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding role by id: {self.role.id}") from re
