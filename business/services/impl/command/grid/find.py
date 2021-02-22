from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.grid.grid_command import GridCommand
from model.grid import Grid


class Find(GridCommand):

    def __init__(self, connection, grid):
        """
        Constructor for class DownloadByContext, from AttachmentCommand
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
