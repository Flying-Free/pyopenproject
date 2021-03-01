from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class QueryService(AbstractService):
    """
    Class QueryService,
    service for query endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find(self, query, offset, page_size, filters, columns, sort_by, group_by,
             show_sums, timeline_visible, timeline_labels, timeline_zoom_level,
             highlighting_mode, highlighted_attributes, show_hierarchies): raise NotImplementedError

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
    def create_form(self, form): raise NotImplementedError

    @abstractmethod
    def schema(self): raise NotImplementedError
