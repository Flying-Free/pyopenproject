from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.user.user_command import UserCommand


class Unlock(UserCommand):

    def __init__(self, identifier):
        self.identifier = identifier

    def execute(self):
        try:
            Connection().delete(f"{self.CONTEXT}/{self.identifier}/lock")
        except RequestError as re:
            raise BusinessError(f"Error unlocking user with id: {self.identifier}") from re
