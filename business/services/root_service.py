from abc import ABCMeta, abstractmethod


class RootService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find(self): raise NotImplementedError
