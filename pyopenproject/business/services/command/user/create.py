from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.user.user_command import UserCommand
from pyopenproject.model import user  as usr


class Create(UserCommand):

    def __init__(self, connection, login, email, first_name, last_name, admin, language, status, password):
        """Constructor for class FindVersions, from ProjectCommand

        :param connection: The connection data
        :param login: The user login
        :param email: The user email address
        :param first_name: The user first name
        :param last_name: The user last name
        :param admin: Is the user an admin
        :param language: The user language
        :param status: The user status
        :param password: The password for the user
        """
        super().__init__(connection)
        self.user = {
            "login": login,
            "email": email,
            "firstName": first_name,
            "lastName": last_name,
            "admin": admin,
            "language": language,
            "status": status,
            "password": password
        }

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}",
                                   json=self.user).execute()
            return usr.User(json_obj)
        except RequestError as re:
            raise BusinessError("Error creating new user") from re
