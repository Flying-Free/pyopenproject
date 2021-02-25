from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import BudgetCommand
from pyopenproject.model import Budget


class Find(BudgetCommand):

    def __init__(self, connection, budget):
        """Constructor for class Find, from BudgetCommand.

        :param connection: The connection data
        :param budget: The budget to find
        """
        super().__init__(connection)
        self.budget = budget

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.budget.id}").execute()
            return Budget(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding budget by id: {self.budget.id}") from re
