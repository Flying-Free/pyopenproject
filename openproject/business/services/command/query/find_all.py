from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.find_list_command import FindListCommand
from openproject.business.services.command.query.query_command import QueryCommand
from openproject.business.util.filters import Filters
from openproject.business.util.url import URL
from openproject.model.query import Query


class FindAll(QueryCommand):

    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def execute(self):
        try:
            request = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               Filters(
                                                                   self.filters)
                                                           ])))
            return FindListCommand(self.connection, request, Query).execute()
            # for tEntry in json_obj["_embedded"]["elements"]:
            #     yield Query(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all queries with filters: {self.filters}") from re
