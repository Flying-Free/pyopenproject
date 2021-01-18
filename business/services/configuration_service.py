from abc import ABCMeta, abstractmethod

from business.services.abstract_service import AbstractService


class ConfigurationService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super(ConfigurationService, self).__init__(connection)

    @abstractmethod
    def find(self): raise NotImplementedError
