from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.patch_request import PatchRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.query.query_command import QueryCommand
from openproject.model.query import Query


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
