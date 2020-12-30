from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.user.user_command import UserCommand
from model.user import User


class Delete(UserCommand):

    def __init__(self, user):
        self.user = user

    def execute(self):
        try:
            json_obj = Connection().delete(f"{self.CONTEXT}/{self.user.id}")
            return User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error deleting user by ID: {self.user.id}") from re