from abc import ABCMeta, abstractmethod


class ConfigurationService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self): raise NotImplementedError
