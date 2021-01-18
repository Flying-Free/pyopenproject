from abc import ABCMeta, abstractmethod


class PriorityService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find(self, priority): raise NotImplementedError

    @abstractmethod
    def find_all(self): raise NotImplementedError
