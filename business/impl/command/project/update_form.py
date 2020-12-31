import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.project.project_command import ProjectCommand
from model.form import Form


class UpdateForm(ProjectCommand):

    def __init__(self, project):
        self.project = project

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}/{self.project.id}/form", json.dumps(self.project.__dict__))
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating project {self.project.name}") from re
