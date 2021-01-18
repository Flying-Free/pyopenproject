from abc import ABCMeta, abstractmethod


class TypeService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find_all(self): raise NotImplementedError

    @abstractmethod
    def find(self, type): raise NotImplementedError
