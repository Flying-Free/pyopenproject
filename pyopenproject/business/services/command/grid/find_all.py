from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.find_list_command import FindListCommand
from pyopenproject.business.services.command.grid.grid_command import GridCommand
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model.grid import Grid


class FindAll(GridCommand):

    def __init__(self, connection, filters, sort_by):
        """Constructor for class FindAll, from GridCommand.

        :param connection: The connection data
        :param filters: The filter parameter
        :param sort_by: The sort by parameter
        """
        super().__init__(connection)
        self.filters = filters
        self.sort_by = sort_by

    def execute(self):
        try:
            request = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               Filters(
                                                                   self.filters),
                                                               URLParameter
                                                               ("sortBy", self.sort_by)
                                                           ])))
            return FindListCommand(self.connection, request, Grid).execute()
            # for grid in json_obj["_embedded"]["elements"]:
            #     yield Grid(grid)
        except RequestError as re:
            raise BusinessError("Error finding all grids") from re
