from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.user.user_command import UserCommand


class Lock(UserCommand):

    def __init__(self, identifier):
        self.identifier = identifier

    def execute(self):
        try:
            Connection().post(f"{self.CONTEXT}/{self.identifier}/lock", None)
        except RequestError as re:
            raise BusinessError(f"Error locking user by id: {self.identifier}") from re
