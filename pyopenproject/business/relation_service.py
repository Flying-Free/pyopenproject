from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class RelationService(AbstractService):
    """
    Class RelationService,
    service for relation endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

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
    def find_schema_by_type(self, relation_type): raise NotImplementedError

    @abstractmethod
    def find_all(self, filters, sort_by): raise NotImplementedError

    @abstractmethod
    def update_form(self, relation, form): raise NotImplementedError
