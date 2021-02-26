from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class CustomObjectService(AbstractService):
    """
    Class CustomObjectService,
    service for custom object endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, custom_object): raise NotImplementedError
