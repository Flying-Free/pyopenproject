from abc import ABCMeta, abstractmethod


class UserPreferencesService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self): raise NotImplementedError

    @abstractmethod
    def update(self, user_preferences): raise NotImplementedError
