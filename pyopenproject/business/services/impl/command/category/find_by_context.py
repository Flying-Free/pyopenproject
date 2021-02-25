from pyopenproject import model as cat
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import CategoryCommand


class FindByContext(CategoryCommand):

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
            return cat.Category(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding category by context: {self.context}") from re
