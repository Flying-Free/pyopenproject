from abc import ABCMeta, abstractmethod

from pyopenproject.business import AbstractService


class PriorityService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, priority): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset, page_size, filters, sort_by): raise NotImplementedError
