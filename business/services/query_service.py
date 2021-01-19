from abc import ABCMeta, abstractmethod

from business.services.abstract_service import AbstractService


class QueryService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find(self, query, offset, pageSize, filters, columns, sortBy, groupBy, showSums, timelineVisible,
             timelineLabels, timelineZoomLevel, highlightingMode,
             highlightedAttributes, showHierarchies): raise NotImplementedError

    @abstractmethod
    def update(self, query): raise NotImplementedError

    @abstractmethod
    def delete(self, query): raise NotImplementedError

    @abstractmethod
    def star(self, query): raise NotImplementedError

    @abstractmethod
    def unstar(self, query): raise NotImplementedError

    @abstractmethod
    def find_all(self, filters): raise NotImplementedError

    @abstractmethod
    def create(self, query): raise NotImplementedError

    @abstractmethod
    def update(self, query): raise NotImplementedError

    @abstractmethod
    def create_form(self, query): raise NotImplementedError

    @abstractmethod
    def schema(self): raise NotImplementedError
