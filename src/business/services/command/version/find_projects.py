from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.get_request import GetRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.find_list_command import FindListCommand
from src.business.services.command.version.version_command import VersionCommand
from src.model.project import Project


class FindProjects(VersionCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            request = GetRequest(self.connection, f"{self.CONTEXT}/available_projects")
            return FindListCommand(self.connection, request, Project).execute()
            # for tEntry in json_obj["_embedded"]["elements"]:
            #     yield p.Project(tEntry)
        except RequestError as re:
            raise BusinessError("Error finding projects available for versions") from re
