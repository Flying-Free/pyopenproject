from abc import ABCMeta, abstractmethod


class TypeService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self): raise NotImplementedError

    @abstractmethod
    def find(self, type): raise NotImplementedError
