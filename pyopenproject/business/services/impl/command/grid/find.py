from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import GridCommand
from pyopenproject.model import Grid


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
