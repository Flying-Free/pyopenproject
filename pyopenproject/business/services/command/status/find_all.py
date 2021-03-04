from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.find_list_command import FindListCommand
from pyopenproject.business.services.command.status.status_command import StatusCommand
from pyopenproject.model.status import Status


class FindAll(StatusCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            request = GetRequest(self.connection, f"{self.CONTEXT}")
            return FindListCommand(self.connection, request, Status).execute()
            # for status in json_obj["_embedded"]["elements"]:
            #     yield Status(status)
        except RequestError as re:
            raise BusinessError("Error finding all statuses") from re
