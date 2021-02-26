from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.query.query_command import QueryCommand
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.model.query import Query


class FindAll(QueryCommand):

    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               Filters(
                                                                   self.filters)
                                                           ]))).execute()

            for tEntry in json_obj["_embedded"]["elements"]:
                yield Query(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all queries with filters: {self.filters}") from re
