from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class PrincipalService(AbstractService):
    """
    Class PrincipalService,
    service for principal endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find_all(self, filters): raise NotImplementedError
