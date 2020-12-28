from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.query.query_command import QueryCommand
from model.query import Query


class Star(QueryCommand):

    def __init__(self, query):
        self.query = query

    def execute(self):
        try:
            json_obj = Connection().patch(f"{self.CONTEXT}/{self.query.id}/star")
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error to star: {self.query.id}") from re
