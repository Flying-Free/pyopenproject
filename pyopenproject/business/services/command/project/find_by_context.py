from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.project.project_command import ProjectCommand
from pyopenproject.model import Project


class FindByContext(ProjectCommand):

    def __init__(self, connection, context):
        super().__init__(connection)
        self.context = context

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.context}").execute()
            return Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding project by context: {self.context}") from re
