import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.project import Project


class Update(ProjectCommand):

    def __init__(self, connection, project):
        super(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{self.project.id}",
                                    json=json.dumps(self.project.__dict__)).execute()
            return Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating project: {self.project.name}") from re
