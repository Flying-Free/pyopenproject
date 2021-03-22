from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.grid.grid_command import GridCommand
from pyopenproject.model.grid import Grid


class Find(GridCommand):

    def __init__(self, connection, grid):
        """Constructor for class Find, from GridCommand.

        :param connection: The connection data
        :param grid: The grid to find
        """
        super().__init__(connection)
        self.grid = grid

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.grid.id}").execute()
            return Grid(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding grid by id: {self.grid.id}") from re
