from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.delete_request import DeleteRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand


class Delete(QueryCommand):

    def __init__(self, connection, query):
        super().__init__(connection)
        self.query = query

    def execute(self):
        try:
            DeleteRequest(self.connection, f"{self.CONTEXT}/{self.query.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error updating query by id: {self.query.id}") from re
