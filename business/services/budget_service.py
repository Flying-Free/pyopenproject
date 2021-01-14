from abc import ABCMeta, abstractmethod


class BudgetService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self, budget): raise NotImplementedError
