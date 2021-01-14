from business.services.budget_service import BudgetService
from business.services.impl.command.budget.find import Find


class BudgetServiceImpl(BudgetService):

    def find(self, budget):
        return Find(budget).execute()
