from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.project.project_command import ProjectCommand
from model.budget import Budget


class FindBudgets(ProjectCommand):

    def __init__(self, project):
        self.project = project

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.project.id}/budgets")
            for budget in json_obj["_embedded"]["elements"]:
                yield Budget(budget)
        except RequestError as re:
            raise BusinessError(f"Error finding project by id: {self.project.name}") from re
