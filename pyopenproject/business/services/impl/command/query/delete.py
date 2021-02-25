from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import DeleteRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import QueryCommand


class Delete(QueryCommand):

    def __init__(self, connection, query):
        super().__init__(connection)
        self.query = query

    def execute(self):
        try:
            DeleteRequest(self.connection, f"{self.CONTEXT}/{self.query.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error updating query by id: {self.query.id}") from re
