import json

import model.work_package as wp
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand


class CreateWorkPackage(ProjectCommand):

    def __init__(self, connection, project, notify, workPackage):
        super().__init__(connection)
        self.project = project
        self.notify = notify
        self.workPackage = workPackage

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}/{self.project.id}/work_packages?{self.notify}",
                                   json=json.dumps(self.workPackage.__dict__)).execute()
            for workPackage in json_obj["_embedded"]["elements"]:
                yield wp.WorkPackage(workPackage)
        except RequestError as re:
            raise BusinessError(f"Error finding work package by id: {self.project.name}") from re
