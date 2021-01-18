from abc import ABCMeta, abstractmethod


class CategoryService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find(self, category): raise NotImplementedError

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

