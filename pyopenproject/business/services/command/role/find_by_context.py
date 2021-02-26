from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.role.role_command import RoleCommand
from pyopenproject.model.role import Role


class FindByContext(RoleCommand):

    def __init__(self, connection, context):
        """Constructor for class FindByContext, from CategoryCommand.

        :param connection: The connection data
        :param context: The URL context
        """
        super().__init__(connection)
        self.context = context

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.context}").execute()
            return Role(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding category by context: {self.context}") from re
