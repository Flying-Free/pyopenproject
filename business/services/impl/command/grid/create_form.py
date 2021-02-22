from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.grid.grid_command import GridCommand


class CreateForm(GridCommand):

    def __init__(self, connection):
        """
        Constructor for class CreateForm, from GridCommand

        :param connection: The connection data
        """
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/form").execute()
            return json_obj
        except RequestError as re:
            raise BusinessError(f"Error creating a grid form") from re
