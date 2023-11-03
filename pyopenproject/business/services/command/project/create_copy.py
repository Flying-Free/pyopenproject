from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.project.project_command import ProjectCommand
from pyopenproject.model import project as p


class CreateCopy(ProjectCommand):

    def __init__(self, connection, project, project_id):
        super().__init__(connection)
        self.project = project
        self.project_id = project_id

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/{self.project_id}/copy",
                                   json=self.project.__dict__).execute()
            return p.Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating project: {self.project.name}") from re
