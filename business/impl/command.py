from abc import ABCMeta, abstractmethod


class Command:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self): raise NotImplementedError
