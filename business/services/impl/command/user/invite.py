import model.user as usr
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user.user_command import UserCommand


class Invite(UserCommand):

    def __init__(self, connection, first_name, email):
        super().__init__(connection)
        self.user = {
            "email": email,
            "firstName": first_name,
            "status": "invited"
        }

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}",
                                   json=self.user).execute()
            return usr.User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating new user") from re
