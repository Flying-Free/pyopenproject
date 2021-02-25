from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import StatusCommand
from pyopenproject.model import Status


class FindByContext(StatusCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            return Status(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding status by context: {self.CONTEXT}") from re
