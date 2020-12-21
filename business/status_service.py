from abc import ABCMeta, abstractmethod


class StatusService(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_by_context(self): raise NotImplementedError

    @abstractmethod
    def find_by_id(self): raise NotImplementedError

    @abstractmethod
    def find_all(self): raise NotImplementedError
