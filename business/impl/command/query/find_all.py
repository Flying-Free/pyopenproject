import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.query.query_command import QueryCommand
from model.query import Query


class FindAll(QueryCommand):

    def __init__(self, filters):
        self.filters = filters

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}?{self.filters}")
            for tEntry in json.loads(json_obj):
                yield Query(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all queries with filters: {self.filters}") from re
