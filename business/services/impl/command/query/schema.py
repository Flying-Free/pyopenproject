from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand


class Schema(QueryCommand):

    def __init__(self, connection):
        """ Constructor for class Schema, from QueryCommand

        :param connection: The connection command
        """
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/schema").execute()
            return Schema(json_obj)
        except RequestError as re:
            raise BusinessError("Error finding schema") from re
