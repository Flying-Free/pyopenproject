import json

from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand
from model.query import Query


class Update(QueryCommand):

    def __init__(self, query):
        self.query = query

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.query.id}", json.dumps(self.project.__dict__))
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating query by id: {self.query.id}") from re
