from abc import ABCMeta, abstractmethod

from business.services.abstract_service import AbstractService


class NewsService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, news): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset, page_size, filters, sort_by): raise NotImplementedError
