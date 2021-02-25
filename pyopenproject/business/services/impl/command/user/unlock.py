from pyopenproject import model as u
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import DeleteRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import UserCommand


class Unlock(UserCommand):

    def __init__(self, connection, user):
        super().__init__(connection)
        self.user = user

    def execute(self):
        try:
            json_obj = DeleteRequest(self.connection, f"{self.CONTEXT}/{self.user.id}/lock").execute()
            return u.User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error unlocking user with id: {self.user.id}") from re
