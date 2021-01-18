from abc import ABCMeta, abstractmethod


class NewsService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find(self, news): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset, pageSize, filters, sortBy): raise NotImplementedError