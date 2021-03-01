from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.user.user_command import UserCommand
from pyopenproject.model import user  as usr


class Invite(UserCommand):

    def __init__(self, connection, first_name, email):
        """Constructor for class Invite, from UserCommand

        :param connection: The connection data
        :param first_name: The user's first name
        :param email: The users's email address
        """
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
            raise BusinessError(f"Error creating inviting user {self.user['email']}") from re
