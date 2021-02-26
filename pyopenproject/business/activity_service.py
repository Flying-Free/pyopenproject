from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class ActivityService(AbstractService):
    """
    Class ActivityService,
    service for activity endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find(self, activity): raise NotImplementedError

    @abstractmethod
    def update(self, activity): raise NotImplementedError
