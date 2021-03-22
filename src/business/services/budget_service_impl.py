from src.business.budget_service import BudgetService
from src.business.services.command.budget.find import Find


class BudgetServiceImpl(BudgetService):
    def __init__(self, connection):
        super().__init__(connection)

    def find(self, budget):
        return Find(self.connection, budget).execute()
