from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class NewsService(AbstractService):
    """
    Class NewsService,
    service for new endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, news): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset=None, page_size=None, filters=None, sort_by=None): raise NotImplementedError
