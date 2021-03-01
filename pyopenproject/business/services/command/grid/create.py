from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.grid.grid_command import GridCommand
from pyopenproject.model.grid import Grid


class Create(GridCommand):

    def __init__(self, connection, grid):
        """Constructor for class Create, from GridCommand.

        :param connection: The connection data
        :param grid: The grid to create
        """
        super().__init__(connection)
        self.grid = grid

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}",
                                   data=self.grid.__dict__).execute()
            return Grid(json_obj)
        except RequestError as re:
            raise BusinessError("Error creating grid") from re
