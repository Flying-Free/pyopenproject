from abc import ABCMeta, abstractmethod


class DocumentService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find(self, document): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset, pageSize, sortBy): raise NotImplementedError
