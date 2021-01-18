from abc import ABCMeta, abstractmethod


class UserPreferencesService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find(self): raise NotImplementedError

    @abstractmethod
    def update(self, user_preferences): raise NotImplementedError
