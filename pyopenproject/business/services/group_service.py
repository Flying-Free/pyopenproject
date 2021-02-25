from abc import ABCMeta, abstractmethod

from pyopenproject.business import AbstractService


class GroupService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, group): raise NotImplementedError