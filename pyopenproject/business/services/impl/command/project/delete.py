from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import DeleteRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import ProjectCommand


class Delete(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            DeleteRequest(self.connection, f"{self.CONTEXT}/{self.project.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error deleting project: {self.project.name}") from re
