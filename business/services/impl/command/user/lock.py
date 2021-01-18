from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user.user_command import UserCommand


class Lock(UserCommand):

    def __init__(self, connection, user):
        super(connection)
        self.user = user

    def execute(self):
        try:
            PostRequest(self.connection, f"{self.CONTEXT}/{self.user.id}/lock").execute()
        except RequestError as re:
            raise BusinessError(f"Error locking user by id: {self.user.id}") from re
