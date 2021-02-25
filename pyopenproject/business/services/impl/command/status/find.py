from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import StatusCommand
from pyopenproject.model import Status


class Find(StatusCommand):

    def __init__(self, connection, status):
        super().__init__(connection)
        self.status = status

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.status.id}").execute()
            return Status(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding status by id: {self.status}") from re
