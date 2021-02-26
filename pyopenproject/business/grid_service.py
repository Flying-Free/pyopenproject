from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class GridService(AbstractService):
    """
    Class GridService,
    service for grid endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, grid): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset, page_size, filters, sort_by): raise NotImplementedError

    @abstractmethod
    def create(self, grid): raise NotImplementedError

    @abstractmethod
    def update(self, grid): raise NotImplementedError

    @abstractmethod
    def create_form(self): raise NotImplementedError
