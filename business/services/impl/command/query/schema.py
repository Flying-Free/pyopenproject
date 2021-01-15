from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand
from model.query import Query


class Schema(QueryCommand):



    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/schema")
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding schema: {self.schema}") from re
