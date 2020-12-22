from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.user.user_command import UserCommand


class Unlock(UserCommand):

    def __init__(self, identifier):
        self.identifier = identifier

    def execute(self):
        try:
            Connection().delete(f"{self.CONTEXT}/{self.identifier}/lock")
        except RequestError as re:
            raise BusinessError(f"Error unlocking user with id: {self.identifier}") from re
