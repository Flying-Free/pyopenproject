import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand
from model.query import Query


class Create(QueryCommand):

    def __init__(self, query):
        self.query = query

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}", json.dumps(self.query.__dict__))
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating query: {self.query}") from re
