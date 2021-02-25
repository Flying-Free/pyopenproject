from pyopenproject import model as usr
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import UserCommand


class Find(UserCommand):

    def __init__(self, connection, user):
        super().__init__(connection)
        self.user = user

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.user.id}").execute()
            return usr.User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding user by ID: {self.user.id}") from re
