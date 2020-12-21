from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.user.user_command import UserCommand
from src.extract.model.user import User


class FindById(UserCommand):

    def __init__(self, identifier):
        self.identifier = identifier

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.identifier}")
            return User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding user by ID: {self.identifier}") from re
