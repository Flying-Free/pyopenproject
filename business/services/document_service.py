from abc import ABCMeta, abstractmethod


class DocumentService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self, document): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset, pageSize, sortBy): raise NotImplementedError
