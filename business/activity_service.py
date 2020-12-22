from abc import ABCMeta, abstractmethod


class ActivityService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find_by_id(self, identifier): raise NotImplementedError

    @abstractmethod
    def update(self, identifier): raise NotImplementedError