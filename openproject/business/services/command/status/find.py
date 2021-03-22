from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.status.status_command import StatusCommand
from openproject.model.status import Status


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
