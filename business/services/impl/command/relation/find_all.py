import json

import model.relation as rel
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.relation.relation_command import RelationCommand


class FindAll(RelationCommand):

    def __init__(self, connection, filters, sortBy):
        super().__init__(connection)
        self.filters = filters
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}?{self.filters},{self.sortBy}").execute()
            for tEntry in json_obj["_embedded"]["elements"]:
                yield rel.Relation(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all queries with filters: {self.filters}") from re
