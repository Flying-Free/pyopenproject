from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.find_list_command import FindListCommand
from openproject.business.services.command.type.type_command import TypeCommand
from openproject.model import Version


class FindVersions(TypeCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            request = GetRequest(self.connection, f"{self.CONTEXT}/{self.project.id}/versions")
            return FindListCommand(self.connection, request, Version).execute()
            # for tEntry in json_obj["_embedded"]["elements"]:
            #     yield Version(tEntry)
        except RequestError as re:
            raise BusinessError("Error finding all time entries") from re
