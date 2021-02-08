from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.grid.grid_command import GridCommand
from model.grid import Grid


class Create(GridCommand):

    def __init__(self, connection, grid):
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
            raise BusinessError(f"Error creating grid") from re
