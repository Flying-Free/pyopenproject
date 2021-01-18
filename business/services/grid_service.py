from abc import ABCMeta, abstractmethod


class GridService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

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