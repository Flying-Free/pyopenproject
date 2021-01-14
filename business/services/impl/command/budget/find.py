from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.budget.budget_command import BudgetCommand
from model.budget import Budget


class Find(BudgetCommand):

    def __init__(self, budget):
        self.budget = budget

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.budget.id}")
            return Budget(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding budget by id: {self.budget.id}") from re
