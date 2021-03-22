from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.get_request import GetRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.user.user_command import UserCommand
from src.model.user import User


class FindByContext(UserCommand):

    def __init__(self, connection, context):
        """
        Contructor for class FindByContext, from UserCommand

        :param connection: The connection data
        :param context: The user's url context
        """
        super().__init__(connection)
        self.context = context

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.context}").execute()
            return User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding user by context: {self.context}") from re
