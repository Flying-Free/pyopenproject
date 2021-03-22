from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.get_request import GetRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.find_list_command import FindListCommand
from src.business.services.command.project.project_command import ProjectCommand
from src.model import Category


class FindCategories(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            request = GetRequest(self.connection, f"{self.CONTEXT}/{self.project.id}/categories")
            return FindListCommand(self.connection, request, Category).execute()
            # for category in json_obj["_embedded"]["elements"]:
            #     yield Category(category)
        except RequestError as re:
            raise BusinessError(f"Error finding categories by project: {self.project.name}") from re
