from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.relation.relation_command import RelationCommand
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model import relation as rel


class FindAll(RelationCommand):

    def __init__(self, connection, filters, sort_by):
        super().__init__(connection)
        self.filters = filters
        self.sort_by = sort_by

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               Filters(
                                                                   self.filters),
                                                               URLParameter("sortBy", self.sort_by)
                                                           ]))).execute()

            for tEntry in json_obj["_embedded"]["elements"]:
                yield rel.Relation(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all queries with filters: {self.filters}") from re
