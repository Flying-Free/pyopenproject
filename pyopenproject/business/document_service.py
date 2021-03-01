from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class DocumentService(AbstractService):
    """
    Class DocumentService,
    service for document endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, document): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset=None, page_size=None, sort_by=None): raise NotImplementedError
