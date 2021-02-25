from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PatchRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import QueryCommand
from pyopenproject.model import Query


class Unstar(QueryCommand):

    def __init__(self, connection, query):
        super().__init__(connection)
        self.query = query

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{self.query.id}/unstar").execute()
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error to unstar: {self.query.id}") from re
