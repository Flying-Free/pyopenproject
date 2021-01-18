import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.relation.relation_command import RelationCommand
from model.relation import Relation


class FindAll(RelationCommand):

    def __init__(self, connection, filters, sortBy):
        super(connection)
        self.filters = filters
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}?{self.filters},{self.sortBy}").execute()
            for tEntry in json.loads(json_obj):
                yield Relation(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all queries with filters: {self.filters}") from re
