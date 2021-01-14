from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.category import Category


class FindCategories(ProjectCommand):

    def __init__(self, project):
        self.project = project

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.project.id}/categories")
            for category in json_obj["_embedded"]["elements"]:
                yield Category(category)
        except RequestError as re:
            raise BusinessError(f"Error finding categories by project: {self.project.name}") from re
