from abc import ABCMeta, abstractmethod

from business.services.abstract_service import AbstractService


class CustomActionService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, custom_action): raise NotImplementedError

    @abstractmethod
    def execute(self, custom_action): raise NotImplementedError
