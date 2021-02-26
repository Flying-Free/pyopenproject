from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.project.project_command import ProjectCommand
from pyopenproject.model.form import Form


class CreateWorkPackageForm(ProjectCommand):

    def __init__(self, connection, project, form):
        super().__init__(connection)
        self.project = project
        self.form = form

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/{self.project.id}/work_packages/form",
                                   json=self.form.__dict__).execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding work package by id: {self.project.name}") from re
