from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.budget.budget_command import BudgetCommand
from model.budget import Budget


class Find(BudgetCommand):

    def __init__(self, connection, budget):
        super().__init__(connection)
        self.budget = budget

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.budget.id}").execute()
            return Budget(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding budget by id: {self.budget.id}") from re
