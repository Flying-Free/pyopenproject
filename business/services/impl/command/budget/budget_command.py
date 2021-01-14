from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class BudgetCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/budgets"

    @abstractmethod
    def execute(self): raise NotImplementedError
