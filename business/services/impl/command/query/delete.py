from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.delete_request import DeleteRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand
from model.query import Query


class Delete(QueryCommand):

    def __init__(self, connection, query):
        super(connection)
        self.query = query

    def execute(self):
        try:
            json_obj = DeleteRequest(self.connection, f"{self.CONTEXT}/{self.query.id}").execute()
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating query by id: {self.query.id}") from re
