from abc import ABCMeta, abstractmethod


class RootService:
    __metaclass__ = ABCMeta


    @abstractmethod
    def find(self): raise NotImplementedError
