import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.form import Form


class CreateWorkPackageForm(ProjectCommand):

    def __init__(self, project, notify, form):
        self.project = project
        self.notify = notify
        self.form = form

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}/{self.project.id}/work_packages/form", json.dumps(self.form.__dict__))
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding work package by id: {self.project.name}") from re
