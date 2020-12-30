from abc import abstractmethod, ABCMeta

from business.impl.command.command import Command


class UserPreferencesCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/my_preferences/"

    @abstractmethod
    def execute(self): raise NotImplementedError
