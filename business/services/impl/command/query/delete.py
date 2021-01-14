from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand
from model.query import Query


class Delete(QueryCommand):

    def __init__(self, query):
        self.query = query

    def execute(self):
        try:
            json_obj = Connection().delete(f"{self.CONTEXT}/{self.query.id}")
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating query by id: {self.query.id}") from re
