from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.delete_request import DeleteRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.project.project_command import ProjectCommand


class Delete(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            DeleteRequest(self.connection, f"{self.CONTEXT}/{self.project.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error deleting project: {self.project.name}") from re
