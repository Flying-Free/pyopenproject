from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.project.project_command import ProjectCommand
from pyopenproject.model import user as usr


class FindAvailableAssignees(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = GetRequest(connection=self.connection,
                                  context=f"{self.CONTEXT}/{self.project.id}/available_assignees") \
                .execute()
            for tEntry in json_obj["_embedded"]["elements"]:
                yield usr.User(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding available_assignees of project: {self.project.name}") from re
