from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.status.status_command import StatusCommand
from pyopenproject.model.status import Status


class FindByContext(StatusCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            return Status(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding status by context: {self.CONTEXT}") from re
