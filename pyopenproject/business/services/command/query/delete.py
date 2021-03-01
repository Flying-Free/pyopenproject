from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.delete_request import DeleteRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.query.query_command import QueryCommand


class Delete(QueryCommand):

    def __init__(self, connection, query):
        super().__init__(connection)
        self.query = query

    def execute(self):
        try:
            DeleteRequest(self.connection, f"{self.CONTEXT}/{self.query.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error updating query by id: {self.query.id}") from re
