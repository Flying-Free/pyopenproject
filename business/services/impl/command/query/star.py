from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand
from model.query import Query


class Star(QueryCommand):

    def __init__(self, connection, query):
        super().__init__(connection)
        self.query = query

    def execute(self):
        try:
            json_obj = PatchRequest(self.connection, f"{self.CONTEXT}/{self.query.id}/star").execute()
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error to star: {self.query.id}") from re
