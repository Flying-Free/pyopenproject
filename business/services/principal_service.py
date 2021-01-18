from abc import ABCMeta, abstractmethod


class PrincipalService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find_all(self, filters): raise NotImplementedError
