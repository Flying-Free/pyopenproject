from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class RootService(AbstractService):
    """
    Class RootService,
    service for root endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self): raise NotImplementedError
