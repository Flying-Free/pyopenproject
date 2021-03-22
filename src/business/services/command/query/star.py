from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.patch_request import PatchRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.query.query_command import QueryCommand
from src.model.query import Query


class Star(QueryCommand):

    def __init__(self, connection, query):
        super().__init__(connection)
        self.query = query

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{self.query.id}/star").execute()
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error to star: {self.query.id}") from re
