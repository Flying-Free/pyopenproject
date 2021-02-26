from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class UserPreferencesService(AbstractService):
    """
    Class UserPreferencesService,
    service for user preferences endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self): raise NotImplementedError

    @abstractmethod
    def update(self, user_preferences): raise NotImplementedError
