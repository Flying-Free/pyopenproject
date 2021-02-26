from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class BudgetService(AbstractService):
    """
    Class BudgetService,
    service for budget endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, budget): raise NotImplementedError
