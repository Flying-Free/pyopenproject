from contextlib import suppress

import model.project as p
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand


class Update(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            project_id = self.project.id
            self.__remove_readonly_attributes()
            json_obj = PatchRequest(connection=self.connection,
                                    headers={"Content-Type": "application/json"},
                                    context=f"{self.CONTEXT}/{project_id}",
                                    json=self.project.__dict__).execute()
            return p.Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating project: {self.project.name}") from re

    def __remove_readonly_attributes(self):
        with suppress(KeyError): del self.project.__dict__["id"]
        with suppress(KeyError): del self.project.__dict__["createdAt"]
        with suppress(KeyError): del self.project.__dict__["updatedAt"]
