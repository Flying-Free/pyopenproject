import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.relation.relation_command import RelationCommand
from model.relation import Relation


class FindAll(RelationCommand):

    def __init__(self, filters, sortBy):
        self.filters = filters
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}?{self.filters},{self.sortBy}")
            for tEntry in json.loads(json_obj):
                yield Relation(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all queries with filters: {self.filters}") from re
