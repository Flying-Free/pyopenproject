from abc import ABCMeta, abstractmethod


class PrincipalService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self, filters): raise NotImplementedError
