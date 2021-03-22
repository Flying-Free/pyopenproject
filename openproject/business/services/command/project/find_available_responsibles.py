from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.find_list_command import FindListCommand
from openproject.business.services.command.project.project_command import ProjectCommand
from openproject.model.user import User


class FindAvailableResponsibles(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            request = GetRequest(self.connection,
                                  f"{self.CONTEXT}/{self.project.id}/available_responsibles")
            return FindListCommand(self.connection, request, User).execute()
            # for tEntry in json_obj["_embedded"]["elements"]:
            #     yield usr.User(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding responsible of project: {self.project.name}") from re
