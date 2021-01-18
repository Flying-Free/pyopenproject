from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.delete_request import DeleteRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user.user_command import UserCommand


class Delete(UserCommand):

    def __init__(self, connection, user):
        super().__init__(connection)
        self.user = user

    def execute(self):
        try:
            DeleteRequest(self.connection, f"{self.CONTEXT}/{self.user.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error deleting user by ID: {self.user.id}") from re
