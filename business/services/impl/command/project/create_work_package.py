import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.work_package import WorkPackage


class CreateWorkPackage(ProjectCommand):

    def __init__(self, project, notify, workPackage):
        self.project = project
        self.notify=notify
        self.workPackage=workPackage

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}/{self.project.id}/work_packages?{self.notify}",json.dumps(self.workPackage.__dict__))
            for workPackage in json_obj["_embedded"]["elements"]:
                yield WorkPackage(workPackage)
        except RequestError as re:
            raise BusinessError(f"Error finding work package by id: {self.project.name}") from re
