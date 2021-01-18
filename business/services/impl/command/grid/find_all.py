from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.grid.grid_command import GridCommand
from model.grid import Grid


class FindAll(GridCommand):

    def __init__(self, connection, offset, pageSize, filters, sortBy):
        super().__init__(connection)
        self.offset = offset
        self.pageSize = pageSize
        self.filters = filters
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = GetRequest(
                self.connection,
                f"{self.CONTEXT}?{self.offset},{self.pageSize},{self.filters},{self.sortBy}").execute()
            for grid in json_obj._embedded.elements:
                yield Grid(grid)
        except RequestError as re:
            raise BusinessError(f"Error finding all grids") from re
