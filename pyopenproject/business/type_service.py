from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class TypeService(AbstractService):
    """
    Class TypeService,
    service for type endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        """Constructor for class TypeService, from AbstractService
        :param connection: The connection data
        """
        super().__init__(connection)

    @abstractmethod
    def find_all(self): raise NotImplementedError

    @abstractmethod
    def find(self, work_package_type): raise NotImplementedError
