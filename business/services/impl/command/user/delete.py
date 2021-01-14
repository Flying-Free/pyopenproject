from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.user.user_command import UserCommand


class Delete(UserCommand):

    def __init__(self, user):
        self.user = user

    def execute(self):
        try:
            Connection().delete(f"{self.CONTEXT}/{self.user.id}")
        except RequestError as re:
            raise BusinessError(f"Error deleting user by ID: {self.user.id}") from re
