from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class RoleService(AbstractService):
    """
    Class RoleService,
    service for role endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find(self, role): raise NotImplementedError

    @abstractmethod
    def find_all(self, filters=None): raise NotImplementedError
