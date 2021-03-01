from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class CustomActionService(AbstractService):
    """
    Class CustomActionService,
    service for custom action endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, custom_action): raise NotImplementedError

    @abstractmethod
    def execute(self, custom_action): raise NotImplementedError
