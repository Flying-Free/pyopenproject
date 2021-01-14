from abc import ABCMeta, abstractmethod


class NewsService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self, news): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset, pageSize, filters, sortBy): raise NotImplementedError