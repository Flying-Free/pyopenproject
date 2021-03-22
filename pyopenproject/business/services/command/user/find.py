from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.user.user_command import UserCommand
from pyopenproject.model import user  as usr


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
