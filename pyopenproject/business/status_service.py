from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class StatusService(AbstractService):
    """
    Class StatusService,
    service for status endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find_by_context(self): raise NotImplementedError

    @abstractmethod
    def find(self, status): raise NotImplementedError

    @abstractmethod
    def find_all(self): raise NotImplementedError
