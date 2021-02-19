from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.grid.grid_command import GridCommand
from model.grid import Grid
from util.Filters import Filters
from util.URL import URL
from util.URLParameter import URLParameter


class FindAll(GridCommand):

    def __init__(self, connection, offset, page_size, filters,
                 sort_by):
        super().__init__(connection)
        self.offset = offset
        self.page_size = page_size
        self.filters = filters
        self.sort_by = sort_by

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               URLParameter("offset", self.offset),
                                                               URLParameter("pageSize", self.page_size),
                                                               Filters("filters", self.filters),
                                                               URLParameter("sortBy", self.sort_by)
                                                           ]))).execute()

            for grid in json_obj["_embedded"]["elements"]:
                yield Grid(grid)
        except RequestError as re:
            raise BusinessError(f"Error finding all grids") from re
