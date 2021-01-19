from abc import ABCMeta, abstractmethod

from business.services.abstract_service import AbstractService


class GridService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, grid): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset, pageSize, filters, sortBy): raise NotImplementedError

    @abstractmethod
    def create(self, grid): raise NotImplementedError

    @abstractmethod
    def update(self, grid): raise NotImplementedError

    @abstractmethod
    def create_form(self, grid): raise NotImplementedError