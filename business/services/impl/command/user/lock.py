import model.user as u
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user.user_command import UserCommand


class Lock(UserCommand):

    def __init__(self, connection, user):
        super().__init__(connection)
        self.user = user

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}/{self.user.id}/lock",
                                   headers={"Content-Type": "application/hal+json"}).execute()
            return u.User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error locking user by id: {self.user.id}") from re
