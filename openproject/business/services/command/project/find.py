from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.project.project_command import ProjectCommand
from openproject.model import project as p


class Find(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.project.id}").execute()
            return p.Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding project by id: {self.project.name}") from re
