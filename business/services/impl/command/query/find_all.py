import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand
from model.query import Query
from util.Filters import Filters
from util.URL import URL


class FindAll(QueryCommand):

    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                          [
                                              Filters("filters", self.filters)
                                          ]))).execute()

            for tEntry in json_obj["_embedded"]["elements"]:
                yield Query(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all queries with filters: {self.filters}") from re
