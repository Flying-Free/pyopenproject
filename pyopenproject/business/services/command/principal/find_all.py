from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.find_list_command import FindListCommand
from pyopenproject.business.services.command.principal.principal_command import PrincipalCommand
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.model.principal import Principal


class FindAll(PrincipalCommand):

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
            return FindListCommand(self.connection, request, Principal).execute()
            # for principal in json_obj["_embedded"]["elements"]:
            #     yield p.Principal(principal)
        except RequestError as re:
            raise BusinessError("Error finding all principals") from re
