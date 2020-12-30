from abc import ABCMeta, abstractmethod


class QueryService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find(self, query,offset,pageSize,filters,columns,sortBy,groupBy,showSums,timelineVisible,timelineLabels,
                     timelineZoomLevel,highlightingMode,highlightedAttributes,showHierarchies): raise NotImplementedError

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
