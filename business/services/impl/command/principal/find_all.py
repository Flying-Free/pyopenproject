import model.principal as p
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.principal.principal_command import PrincipalCommand
from util.Filters import Filters
from util.URL import URL


class FindAll(PrincipalCommand):

    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               Filters("filters", self.filters)
                                                           ]))).execute()

            for principal in json_obj["_embedded"]["elements"]:
                yield p.Principal(principal)
        except RequestError as re:
            raise BusinessError(f"Error finding all principals") from re
