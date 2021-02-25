from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PatchRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import GridCommand
from pyopenproject.model import Grid


class Update(GridCommand):

    def __init__(self, connection, grid):
        """Constructor for class Update, from GridCommand.

        :param connection: The connection data
        :param grid: The grid to update
        """
        super().__init__(connection)
        self.grid = grid

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    headers={"Content-Type": "application/json"},
                                    context=f"{self.CONTEXT}",
                                    json=self.grid.__dict__).execute()
            return Grid(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating grid with id: {self.grid.id}") from re
