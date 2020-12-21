from abc import ABCMeta, abstractmethod


class GroupService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError
