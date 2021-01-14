from abc import ABCMeta, abstractmethod


class RoleService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find(self, role): raise NotImplementedError

    @abstractmethod
    def find_all(self, role): raise NotImplementedError
