
import model.project as p
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand


class Update(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    headers={"Content-Type": "application/json"},
                                    context=f"{self.CONTEXT}/{self.project.id}",
                                    json=self.project.__dict__).execute()
            return p.Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating project: {self.project.name}") from re
