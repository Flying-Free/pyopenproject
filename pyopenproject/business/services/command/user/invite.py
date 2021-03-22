from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.user.user_command import UserCommand
from pyopenproject.model import user  as usr


class Invite(UserCommand):

    def __init__(self, connection, email, login, first_name, last_name, admin, language):
        """Constructor for class Invite, from UserCommand

        :param connection: The connection data
        :param email: The users's email address
        :param login: The user's login
        :param first_name: The user's first name
        :param last_name: The user's last name
        :param admin: True if the user is an admin
        :param language: The application language for the user

        """
        super().__init__(connection)
        self.user = {
            "email": email,
            "admin": admin,
            "language": language,
            "status": "invited"
        }
        if login:
            self.user["login"] = login
        if first_name:
            self.user["firstName"] = first_name
        if last_name:
            self.user["lastName"] = last_name


    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}",
                                   json=self.user).execute()
            return usr.User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating inviting user {self.user['email']}") from re
