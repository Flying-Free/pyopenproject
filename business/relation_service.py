from abc import ABCMeta, abstractmethod


class RelationService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find(self, relation): raise NotImplementedError

    @abstractmethod
    def update(self, relation): raise NotImplementedError

    @abstractmethod
    def delete(self, relation): raise NotImplementedError

    @abstractmethod
    def find_schema(self): raise NotImplementedError

    @abstractmethod
    def find_schema(self, type): raise NotImplementedError

    @abstractmethod
    def find_all(self, filters, sortBy): raise NotImplementedError

    @abstractmethod
    def update_form(self, relation): raise NotImplementedError