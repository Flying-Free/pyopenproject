from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import QueryCommand


class Schema(QueryCommand):

    def __init__(self, connection):
        """Constructor for class Schema, from QueryCommand

        :param connection: The connection command
        """
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/schema").execute()
            return Schema(json_obj)
        except RequestError as re:
            raise BusinessError("Error finding schema") from re
