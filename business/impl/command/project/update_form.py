import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.project.project_command import ProjectCommand
from model.project import Project


class UpdateForm(ProjectCommand):

    def __init__(self, project, form):
        self.project = project
        self.form = form

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}/{self.project.id}/form", json.dumps(self.form.__dict__))
            return Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating form: {self.form.name} for project {self.project.name}") from re
