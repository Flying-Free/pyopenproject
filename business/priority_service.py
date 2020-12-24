from abc import ABCMeta, abstractmethod


class PriorityService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self, priority): raise NotImplementedError

    @abstractmethod
    def find_all(self): raise NotImplementedError
