from abc import ABCMeta, abstractmethod

from pyopenproject.business import AbstractService


class CategoryService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        """Constructor of abstract class CategoryService, from AbstractService

        :param connection: The connection data
        """
        super().__init__(connection)

    @abstractmethod
    def find(self, category): raise NotImplementedError

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError