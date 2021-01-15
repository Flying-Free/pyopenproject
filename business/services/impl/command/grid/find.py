from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.grid.grid_command import GridCommand
from model.grid import Grid


class Find(GridCommand):

    def __init__(self, grid):
        self.grid = grid

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.grid.id}")
            return Grid(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding grid by id: {self.grid.id}") from re
