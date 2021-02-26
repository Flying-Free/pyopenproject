from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.project.project_command import ProjectCommand
from pyopenproject.model import Category


class FindCategories(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.project.id}/categories").execute()
            for category in json_obj["_embedded"]["elements"]:
                yield Category(category)
        except RequestError as re:
            raise BusinessError(f"Error finding categories by project: {self.project.name}") from re
