from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class HelpTextsService(AbstractService):
    """
    Class HelpTextsService,
    service for help text endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, help_text): raise NotImplementedError

    @abstractmethod
    def find_all(self): raise NotImplementedError
