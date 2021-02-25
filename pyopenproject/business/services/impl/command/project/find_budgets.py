from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import ProjectCommand
from pyopenproject.model import Budget


class FindBudgets(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.project.id}/budgets").execute()
            for budget in json_obj["_embedded"]["elements"]:
                yield Budget(budget)
        except RequestError as re:
            raise BusinessError(f"Error finding budgets by id: {self.project.name}") from re
