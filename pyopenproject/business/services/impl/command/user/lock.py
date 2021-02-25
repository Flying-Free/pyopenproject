from pyopenproject import model as u
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import UserCommand


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
