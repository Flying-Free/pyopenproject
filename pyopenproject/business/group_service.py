from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class GroupService(AbstractService):
    """
    Class GroupService,
    service for group endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, group): raise NotImplementedError
