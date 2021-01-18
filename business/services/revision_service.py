from abc import ABCMeta, abstractmethod


class RevisionService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find(self, revision): raise NotImplementedError