from abc import ABCMeta, abstractmethod


class GroupService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self, group): raise NotImplementedError