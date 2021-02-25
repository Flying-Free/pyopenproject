
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import ProjectCommand
from pyopenproject.model import Form


class UpdateForm(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/{self.project.id}/form",
                                   json=self.project.__dict__).execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating project form {self.project.name}") from re
