import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.form import Form


class CreateWorkPackageForm(ProjectCommand):

    def __init__(self, connection, project, notify, form):
        super(connection)
        self.project = project
        self.notify = notify
        self.form = form

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}/{self.project.id}/work_packages/form",
                                   json=json.dumps(self.form.__dict__)).execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding work package by id: {self.project.name}") from re
