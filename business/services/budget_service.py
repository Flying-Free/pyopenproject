from abc import ABCMeta, abstractmethod


class BudgetService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find(self, budget): raise NotImplementedError
