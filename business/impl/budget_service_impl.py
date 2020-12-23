from business.budget_service import BudgetService
from business.impl.command.budget.find import Find


class BudgetServiceImpl(BudgetService):

    def find(self, budget):
        return Find(budget).execute()
