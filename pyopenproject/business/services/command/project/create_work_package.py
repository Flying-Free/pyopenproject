from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.project.project_command import ProjectCommand
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model import work_package as wp


class CreateWorkPackage(ProjectCommand):

    def __init__(self, connection, project, work_package, notify):
        super().__init__(connection)
        self.project = project
        self.work_package = work_package
        self.notify = notify

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=str(URL(f"{self.CONTEXT}/{self.project.id}/work_packages",
                                                   [URLParameter
                                                    ("notify", self.notify)])
                                               ),
                                   json=self.work_package.__dict__).execute()
            return wp.WorkPackage(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding work package by id: {self.project.name}") from re
