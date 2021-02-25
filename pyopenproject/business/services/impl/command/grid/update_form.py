from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import GridCommand
from pyopenproject.model import Grid


class UpdateForm(GridCommand):

    def __init__(self, connection, grid, grid_form):
        """Constructor for class UpdateForm, from GridCommand.

        :param connection: The connection data
        :param grid: The grid
        :param grid_form: The grid form to update
        """
        super().__init__(connection)
        self.grid = grid
        self.grid_form = grid_form

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/{self.grid.id}/form",
                                   json=self.grid_form).execute()
            return Grid(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating grid by id: {self.grid.id}") from re
